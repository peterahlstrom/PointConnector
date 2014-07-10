# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PointConnector
                                 A QGIS plugin
 Draw lines between points
                             -------------------
        begin                : 2014-06-12
        copyright            : (C) 2014 Peter Ahlstrom
        email                : ahlstrom.peter@gmail.com

 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    #Load PointConnector class from file PointConnector.
    from .point_connector import PointConnector
    return PointConnector(iface)
