PointConnector
==============

A QGIS plugin used for creating lines between points following a from-to list.

Usage
-------

Inputs:
An ESRI shape-file with points. The first (or only) field should contain the joining attribute found in the csv-file.
A comma separated txt-file (CSV-file) formatted like this: [from], [to]. Each row results in a straight line between the two corresponding points.
When using special characters make sure the file is saved with utf-8 encoding.

Example:

Stockholm, Paris

London, New York

Paris, London

...

Output:
A layer with lines, each with from- and to-attributes.


Background
----------

PointConnector is the result of a problem I faced working with a geographical analysis for the local school authority. I needed to show the distance between kids homes and preschool on a map, each kid represented with a line from their home to the school. A total of 18 000 lines needed to be drawn, and it should be easy making a new version of the map each semester. My input was the schools register and georeferenced addresses for the city.
The result is a basis for analysis, for planning new school locations and seeing other patterns.

PointConnector has also shown to be a useful tool for creating input to the FME transformer [ShortestPathFinder](http://fmepedia.safe.com/articles/Samples_and_Demos/Find-the-Shortest-Path-Between-a-Start-and-End-Point)


Licence
-------

This plugin was developed by Peter Ahlstrom in 2014.
It is free software and licensed under the GNU General Public Licence v2.


Bugs and contact
----------------

Bug reports and suggestions can be sent to 
ahlstrom (dot) peter (at) gmail (dot) com 

You can also report problems at the issue tracker on github:
https://github.com/peterahlstrom/PointConnector/issues


The plugin was made using the QGIS Plugin Builder: http://hub.qgis.org/projects/plugin-builder
