# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stats.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Statistics(object):
    def setupUi(self, Statistics):
        Statistics.setObjectName("Statistics")
        Statistics.resize(250, 100)        
        self.widget = QtWidgets.QWidget(Statistics)
        self.widget.setGeometry(QtCore.QRect(22, 12, 201, 68))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1)

        self.retranslateUi(Statistics)
        QtCore.QMetaObject.connectSlotsByName(Statistics)

    def retranslateUi(self, Statistics):
        _translate = QtCore.QCoreApplication.translate
        Statistics.setWindowTitle(_translate("Statistics", "Dialog"))       
        self.label.setText(_translate("Statistics", "Avg session duration:"))
        self.label_2.setText(_translate("Statistics", "TextLabel"))
        self.label_3.setText(_translate("Statistics", "Max session duration:"))
        self.label_4.setText(_translate("Statistics", "TextLabel"))
        self.label_5.setText(_translate("Statistics", "Number of sessions:"))
        self.label_6.setText(_translate("Statistics", "TextLabel"))

