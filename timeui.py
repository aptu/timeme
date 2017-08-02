# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'time.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be losqtSLottyQt!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

class Ui_TimeMe(object):
    def setupUi(self, TimeMe):
        TimeMe.setObjectName("TimeMe")
        TimeMe.resize(407, 90)
        TimeMe.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        TimeMe.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.horizontalLayout = QtWidgets.QHBoxLayout(TimeMe)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnWork = QtWidgets.QPushButton(TimeMe)
        self.btnWork.setObjectName("btnWork")
        self.btnWork.clicked.connect(self.click_work)
        
        self.horizontalLayout.addWidget(self.btnWork)
        self.btnRelax = QtWidgets.QPushButton(TimeMe)
        self.btnRelax.setObjectName("btnRelax")
        self.btnRelax.clicked.connect(self.click_relax)
        
        self.horizontalLayout.addWidget(self.btnRelax)
        self.btnPause = QtWidgets.QPushButton(TimeMe)
        self.btnPause.setObjectName("btnPause")
        self.btnPause.clicked.connect(self.click_pause)
        
        self.horizontalLayout.addWidget(self.btnPause)

        self.retranslateUi(TimeMe)
        QtCore.QMetaObject.connectSlotsByName(TimeMe)
        
    @pyqtSlot()
    def click_work(self):
        print("Work button clicked")
        
    @pyqtSlot()
    def click_relax(self):
        print("Relax button clicked")
        
    @pyqtSlot()
    def click_pause(self):
        print("Pause button clicked")

    def retranslateUi(self, TimeMe):
        _translate = QtCore.QCoreApplication.translate
        TimeMe.setWindowTitle(_translate("TimeMe", "TimeMe"))
        self.btnWork.setText(_translate("TimeMe", "Work"))
        self.btnRelax.setText(_translate("TimeMe", "Relax"))
        self.btnPause.setText(_translate("TimeMe", "Pause"))

