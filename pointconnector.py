# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PointConnector

 A QGIS plugin used for creating lines between points following a from-to list
                              -------------------
        begin                : 2014-07-01
        copyright            : (C) 2014 by Peter Ahlstrom
        email                : ahlstrom dot peter at gmail dot com
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

# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from pointconnectordialog import PointConnectorDialog
import os.path


class PointConnector:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'pointconnector_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = PointConnectorDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/pointconnector/icon.png"),
            u"Point Connector", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Point Connector", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Point Connector", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            csvPath = self.dlg.csvFileName
            pointPath = self.dlg.pointFileName
         


            point_layer = QgsVectorLayer(pointPath, 'points', 'ogr') #shp-file with attribute field name
            lines_layer = QgsVectorLayer('LineString', 'lines', 'memory') 
            lines_file = csvPath
            
            point_name_index = 0


            pr = lines_layer.dataProvider()
            lines_layer.startEditing()
            pr.addAttributes ([ QgsField('id', QVariant.Int), QgsField('from', QVariant.String), QgsField('to', QVariant.String), QgsField('number', QVariant.Int) ] )

            #creating point coordinate dict
            points = processing.features(point_layer)
            points_dict = {}
            
             #Progress bar widget
            progressMessageBar = iface.messageBar().createMessage("Building point database...")
            progress = QProgressBar()
            progress.setMaximum(len(points))
            progress.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
            progressMessageBar.layout().addWidget(progress)
            iface.messageBar().pushWidget(progressMessageBar, iface.messageBar().INFO)

            #print 'Reading coordinates from points...'
            i = 0
            for p in points:
                geom = p.geometry()
                attrs = p.attributes()
                p = geom.asPoint()
                time.sleep(0.01)
                points_dict[attrs[point_name_index]] = p #attrs[point_name_index] = name field
                i += 1
                progress.setValue(i)
            #print 'Done!\n'
            iface.messageBar().clearWidgets()
            QgsMapLayerRegistry().instance().addMapLayer(point_layer)

            #creating lines list from file
            lines_list = []
            f = codecs.open(lines_file, encoding='utf-8') # utf-8 eller latin-1
            for line in f:
              line = line.split('\n')
              for s in line[:1]:
                s = tuple(s.split(','))
                lines_list.append(s)
            f.close()
            print 'list done'



            #for debug
            #lines_list = lines_list[:100]


            #Progress bar widget
            progressMessageBar = iface.messageBar().createMessage("Drawing lines...")
            progress = QProgressBar()
            progress.setMaximum(len(lines_list))
            progress.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
            progressMessageBar.layout().addWidget(progress)
            iface.messageBar().pushWidget(progressMessageBar, iface.messageBar().INFO)

            #drawing lines
            i = 1
            not_processed_list = []
            
            for line in lines_list:
              if (line[0] in points_dict.keys() and line[1] in points_dict.keys()):
                #print 'drawing', line[0], 'to', line[1]+'...', '('+str(i), 'of', str(len(lines_list))+')'
                frPoint = points_dict[line[0]]
                toPoint = points_dict[line[1]]
                if line[2]:
                    attrs = [i, line[0], line[1], line[2]]
                else:
                    attrs = [i, line[0], line[1]]
                new_line = QgsGeometry.fromPolyline([QgsPoint(frPoint), QgsPoint(toPoint)])
                feat = QgsFeature()
                feat.setGeometry(new_line)
                feat.setAttributes(attrs)
                (res, outFeats) = pr.addFeatures([feat])
                lines_layer.commitChanges()
                if res != True:
                    pass
                    #print 'Something went wrong with', outFeats
                i += 1
                progress.setValue(i)
              else:
                not_processed_list.append(line)
            
                
            iface.messageBar().clearWidgets()

            # add lines layer to canvas
            QgsMapLayerRegistry().instance().addMapLayer(lines_layer)
            

            #print 'Done!', '\n'*2

            if not not_processed_list:
                QMessageBox.information(None, 'Success', 'All lines drawn without error')
            else:     
                error_list = []
                for line in not_processed_list:
                    output_line = line[0], 'to', line[1]
                    error_list.append(str(output_line))                    
                QMessageBox.information(None, 'Error', str(len(not_processed_list))+' out of '+str(len(lines_list))+' line(s) not drawn.')
                #QMessageBox.information(None, 'Error', 'Elements not processed:'+ str(error_list)
