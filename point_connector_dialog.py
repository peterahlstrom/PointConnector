# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PointConnectorDialog
                                 A QGIS plugin
 Creating lines between points following a from-to list.
                             -------------------
        begin                : 2014-07-15
        git sha              : $Format:%H$
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

from PyQt4 import QtGui, uic

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'point_connector_dialog_base.ui'))


class PointConnectorDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(PointConnectorDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.browsePointButton.clicked.connect(self.browsePointButton_clicked)            
        self.browseCsvButton.clicked.connect(self.browseCsvButton_clicked)
        

# Browse Point button

    def browsePointButton_clicked(self):
        pointFileName = QtGui.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        self.pointPathLineEdit.setText(pointFileName)
        self.pointFileName = pointFileName


# Browse CSV button

    def browseCsvButton_clicked(self):
        csvFileName = QtGui.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        self.csvPathLineEdit.setText(csvFileName)
        self.csvFileName = csvFileName
