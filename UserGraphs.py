"""
Wayfindr Hackathon, define user profiles and update navigation graphs
Python Test Code
Author: Georgia Bateman & Team Supercool
Date: 14/11/18
"""

#Load modules
import csv

#Define user class
class User:
	def __init__(self,name,sign,dim,crowd,stairs,esc,lift):
		self.name = name #name of user, string
		self.sign = sign #Bool, is signage hard to read?
		self.dim = dim #bool, avoid dimly lit areas
		self.crowd = crowd #bool, avoid congested areas
		self.stairs = stairs #bool, stairs ok?
		self.esc = esc #bool, escalators ok?
		self.lift = lift #bool, lift preferred to escs

#Initialise user test cases
JeanMarc = User("Jean Marc",0,1,1,1,1,0)
Georgia = User("Georgia",1,0,0,1,1,1)
Alastair = User("Alastair",0,0,1,1,0,1)
Test = User("Test",1,1,1,0,0,1)

#Functions to alter individual user graphs
#Weight dim paths more
def alter_dim(user,graph):
	if user.dim == True: #If user wants to avoid dimly lit routes
		new_graph = graph.copy()
		for edge in new_graph:
			if edge[2] == False: #Dimly lit
				edge[1] = edge[1]*10
		return(new_graph)
	else:
		return(graph)

#Remove paths with stairs
def alter_stairs(user,graph):
	if user.stairs == False: #If user cannot use stairs
		new_graph = graph.copy()
		out_graph = []
		for edge in new_graph:
			if edge[3] == False: #Test if stairs not on edge
				out_graph.append(edge)
		return(out_graph)
	else:
		return(graph)

#Remove paths with escalators
def alter_escs(user,graph):
	if user.esc == False: #If user cannot use escalators
		new_graph = graph.copy()
		out_graph = []
		for edge in new_graph:
			if edge[5] == False:#Test if escalators not on edge
				out_graph.append(edge)
		return(out_graph)
	else:
		return(graph)

#Weight preference of lift vs. escalator
def alter_lift(user,graph):
	if user.lift == True: #Test if user prefers lifts
		new_graph = graph.copy()
		for edge in new_graph:
			if edge[5] == True: #Test if escalator on edge
				edge[1] = edge[1]*10
		return(new_graph)
	else:
		return(graph)

#Weight crowded routes
def alter_crowd(user,graph):
	if user.crowd == True: #Test if user wants to avoid crowded areas
		new_graph = graph.copy()
		for edge in new_graph:
			edge[1] = edge[1]*edge[6] #Multiply edges by crowding weights
		return(new_graph)
	else:
		return(graph)

#Function to create new graphs for each user based on preference 
def compute_update_graphs(user,graph):
	stairs_graph = alter_stairs(user,graph) #Remove stairs if neccessary
	escs_graph = alter_escs(user, stairs_graph) #Remove escalators 
	lift_graph = alter_lift(user,escs_graph) #Prefer lifts
	dim_graph = alter_dim(user,lift_graph) #Prefer brighter routes
	crowd_graph = alter_crowd(user, dim_graph) #Prefer less crowded routes
	return(crowd_graph)


############################################
################TEST CASE###################
############################################

#Import station graph, .csv file format, table with the following row names:
#Start Beacon Id: String
#End Beacon ID: String 
#Path ID: String
#Travel Time: Integer 
#Light Level: Bool, 0 = low, 1 = high
#Stair Count: Bool, 0 = no stairs, 1 = stairs 
#Lift: Bool, 0 = no lift, 1 = lift
#Escalator: Bool, 0 = no escalator, 1 = escalator,
#Crowding: Integer [1,10], 1 = low crowding, 10 = high crowding

graph = []
with open('weightings.csv', 'r') as csvfile:
	testreader = csv.reader(csvfile, delimiter=',')
	for row in testreader: 
		graph.append([row[2],int(float(row[3])),int(float(row[4])),int(float(row[5])),int(float(row[6])),int(float(row[7])),int(float(row[8]))])

#Now create graphs for individual test cases
JeanMarcGraph = compute_update_graphs(JeanMarc,graph)
GeorgiaGraph = compute_update_graphs(Georgia,graph)
AlastairGraph = compute_update_graphs(Alastair,graph)
TestGraph = compute_update_graphs(Test,graph)

#Remove weighting information from graphs


#write new graphs with weightings to .csv files
JeanMarcExport = []
for row in JeanMarcGraph:
	JeanMarcExport.append([row[0],row[1]])

with open('JeanMarcGraph.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['PathID','TravelTimePathWeight'])
	writer.writerows(JeanMarcGraph)







