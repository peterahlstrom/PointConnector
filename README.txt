PointConnector
==============

A QGIS plugin used for creating lines between points following a from-to list.


Usage
-------

Inputs:
An ESRI shape-file with points. The first (or only) field should contain the joining attribute found in the csv-file.
A comma separated txt-file (CSV-file) formatted like this: [from], [to]. Each row results in a straight line between the two corresponding points.

Example:
Stockholm, Paris
London, New York
Paris, London
...

Output:
A layer with lines, each with from- and to-attributes.


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
