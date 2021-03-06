# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PointConnectorDialog
                                 A QGIS plugin
 Creating lines between points following a from-to list.
                             -------------------
        begin                : 2014-07-15
        copyright            : (C) 2014 by Peter Ahlstrom
        email                : ahlstrom (dot) peter (at) gmail (dot) com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt5 import QtGui, uic, QtCore,QtWidgets
from qgis.utils import iface
from qgis.core import QgsProject

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'point_connector_dialog_base.ui'))


class PointConnectorDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        #Constructor
        super(PointConnectorDialog, self).__init__(parent)
        self.settings = QtCore.QSettings("petahl", "PointConnector")
        self.setupUi(self)
        self.browsePointButton.clicked.connect(self.browsePointButton_clicked)            
        self.browseCsvButton.clicked.connect(self.browseCsvButton_clicked)
    def unload(self):
        try:
            self.browsePointButton.clicked.disconnect(self.browsePointButton_clicked)            
            self.browseCsvButton.clicked.disconnect(self.browseCsvButton_clicked)
        except:
            pass
        
    # Browse Point button
    def browsePointButton_clicked(self):
        lastShapeDir = self.settings.value("lastShapeDir", ".")
        pointFileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', lastShapeDir, 'ESRI Shape files (*.shp)')
        self.pointPathLineEdit.setText(pointFileName[0])
        (shpDir, shpFile) = os.path.split(pointFileName[0])
        self.settings.setValue("lastShapeDir", shpDir)

    # Browse CSV button
    def browseCsvButton_clicked(self):
        lastCsvDir = self.settings.value("lastCsvDir", ".")
        csvFileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', lastCsvDir, 'Text files (*.csv *.txt)')
        self.csvPathLineEdit.setText(csvFileName[0])
        (csvDir, csvFile) = os.path.split(csvFileName[0])
        self.settings.setValue("lastCsvDir", csvDir)

    # Populate comboBox
    def populateComboBox(self):
        self.pointsComboBox.clear()
        self.csvComboBox.clear()
        
        points, csv = ['Choose layer...'], ['Choose layer...']
        #for layer in iface.mapCanvas().layers():
        layerMap = QgsProject.instance().mapLayers()
        for name, layer in layerMap.items():
            if hasattr(layer, 'geometryType'):
                if layer.geometryType() == 0: 
                    points.append(layer.name())
                elif layer.geometryType() == 4:
                    csv.append(layer.name())


        self.pointsComboBox.addItems(points)
        self.csvComboBox.addItems(csv)
