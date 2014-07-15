# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PointConnector
                                 A QGIS plugin
 Creating lines between points following a from-to list.
                             -------------------
        begin                : 2014-07-15
        copyright            : (C) 2014 by Peter Ahlstrom
        email                : ahlstrom (dot) peter (at) gmail (dot) com
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load PointConnector class from file PointConnector.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .point_connector import PointConnector
    return PointConnector(iface)
