# Convert the Python output to correct graphML

## rationale 
The following is an explanation of how we had been converting the output from our Python script into a format usable by the Wayfindr SDK.

Our latest script outputs in CSV but still needs some conversion to be the correct GraphML structure.

this is emulating the internal process that would update the weights and values for an individual user - in a real world situation we would become a layer on top of Wayfinder.

Following "Calibration" by the user (i.e., data collection on their particular needs) 

We would use this to update the coefficients used to work out the weights between each node for a particular user - according to a hierachy of criticality to their impairments/preferences.

Currently we have a fairly niave implementation, but with a little bit of work we would either create a library that Wayfindr used, or a plugin or standard for Indoor Positioning Systems to use for supporting accessibility.

## Start with python output 

```
[['1013TO1016', 5, 1, 0, 0, 0, 1], ['1008TO1016', 5000, 0, 0, 0, 0, 10], ['1008TO1002', 405, 1, 1, 0, 0, 9], ['1002TO1008', 320, 1, 1, 0, 0, 8...

```

## Turn it into csv tuples

```
1013TO1016, 5, 1, 0, 0, 0, 1
1008TO1016, 5000, 0, 0, 0, 0, 10
1008TO1002, 405, 1, 1, 0, 0, 9
```
## Add the correct headers

This will make the CSV have the correct fields

```
id, source, target, beginning, middle, end, travel_time, dim, stairs, escs, lift, crowd
```

which should yield something like this: 

```
id, source, target, beginning, middle, end, travel_time, dim, stairs, escs, lift, crowd
1013TO1016, 5, 1, 0, 0, 0, 1
1008TO1016, 5000, 0, 0, 0, 0, 10
1008TO1002, 405, 1, 1, 0, 0, 9
```
Which is the right CSV in the right format

## Regex for ids

Convert the `X-TO-Y` id into multiple fields for source and target using this regex:

```
\n((\d\d\d\d)TO(\d\d\d\d))
```

and replace with:

```
$1, $2, $3, $1b, $1, $1e, 
```

Which gives you the following CSV with the correct fields:

```
id, source, target, beginning, middle, end, travel_time, dim, stairs, escs, lift, crowd
1013TO1016, 1013, 1016, 1013TO1016b, 1013TO1016, 1013TO1016e,  5, 1, 0, 0, 0, 1
1008TO1016, 1008, 1016, 1008TO1016b, 1008TO1016, 1008TO1016e,  5000, 0, 0, 0, 0, 10
1008TO1002, 1008, 1002, 1008TO1002b, 1008TO1002, 1008TO1002e,  405, 1, 1, 0, 0, 9
1002TO1008, 1002, 1008, 1002TO1008b, 1002TO1008, 1002TO1008e,  320, 1, 1, 0, 0, 8
1002TO1009, 1002, 1009, 1002TO1009b, 1002TO1009, 1002TO1009e,  245, 1, 0, 0, 0, 7
```

Now take this new CSV and convert to XML with this http://convertcsv.com/csv-to-xml.htm (because we're using that exact structure)

## Fix the edge attribute

Then correct the full XML Element with this to get the desired structure 

```
\s\s<row>\n\s\s\s\s<id>((\d\d\d\dTO\d\d\d\d))<\/id>\n\s\s\s\s<source>\s(\d\d\d\d)<\/source>\n(\s\s\s\s)<target>\s(\d\d\d\d)<\/target>\n\s\s\s\s<beginning>.*?<\/beginning>\n\s\s\s\s<middle>.*?<\/middle>\n\s\s\s\s<end>.*?<\/end>\n\s\s\s\s<travel_time>(.*?)<\/travel_time>\n\s\s\s\s<dim>(.*?)<\/dim>\n\s\s\s\s<stairs>(.*?)<\/stairs>\n\s\s\s\s<escs>(.*?)<\/escs>\n\s\s\s\s<lift>(.*?)<\/lift>\n\s\s\s\s<crowd>(.*?)<\/crowd>
```

## Now replace with 

```
  <edge id="$2" source="$3" target="$5">
  <data key="beginning">$2b</data>
  <data key="middle">$2m</data>
  <data key="end">$2e</data>
  <data key="travel_time">$6</data>
  <data key="dim">$7</data>
  <data key="stairs">$8</data>
  <data key="escs">$9</data>
  <data key="lift">$10</data>
  <data key="crowd">$11</data>
  <data key="language">en-GB</data>
  </edge>
```

To get the following GraphML

```
<edge id="1008TO1002" source="1008" target="1002">
  <data key="beginning">1008TO1002b</data>
  <data key="middle">1008TO1002m</data>
  <data key="end">1008TO1002e</data>
  <data key="travel_time"> 405</data>
  <data key="dim"> 1</data>
  <data key="stairs"> 1</data>
  <data key="escs"> 0</data>
  <data key="lift"> 0</data>
  <data key="crowd"> 9</data>
  <data key="language">en-GB</data>
  </edge>
<edge id="1002TO1008" source="1002" target="1008">
  <data key="beginning">1002TO1008b</data>
  <data key="middle">1002TO1008m</data>
  <data key="end">1002TO1008e</data>
  <data key="travel_time"> 320</data>
  <data key="dim"> 1</data>
  <data key="stairs"> 1</data>
  <data key="escs"> 0</data>
  <data key="lift"> 0</data>
  <data key="crowd"> 8</data>
  <data key="language">en-GB</data>
  </edge>
```

## debugging edge nodes

  (replace without extras for debugging)

```
  <edge id="$2" source="$3" target="$5">
  <data key="beginning">$2b</data>
  <data key="middle">$2m</data>
  <data key="end">$2e</data>
  <data key="travel_time">$6</data>
  </edge>

```
