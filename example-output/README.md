# Example output explanation and usage

In an ideal system, we would just update on the fly relating to stored coefficients for the User after they input their preferences.

In this particular implementation we have simplified everything by simply replacing the content of the graphML files so that our newly calculated edges are taken used for Pathfinding.

> We could have used the data from the JSON API, but it meant solving a problem that didn't add any value for this proof of concept - i.e., parsing a REST API and ensuring Wayfindr updates accordingly.

Our current script creates sample input for multiple users that will get different experiences, to view from another's perspective, simply replace the edges in the graphML file with the content of one of these XML files. 

The weightings taken from the original input file of weightings (i.e., that would be our ground truth that we recalculate from)
