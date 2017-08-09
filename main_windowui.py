# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'time.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TimeMe(object):
    def setupUi(self, TimeMe):
        TimeMe.setObjectName("TimeMe")
        TimeMe.resize(573, 49)
        TimeMe.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        TimeMe.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.horizontalLayout = QtWidgets.QHBoxLayout(TimeMe)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnWork = QtWidgets.QPushButton(TimeMe)
        self.btnWork.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnWork.setAutoFillBackground(True)
        self.btnWork.setCheckable(True)
        self.btnWork.setChecked(True)
        self.btnWork.setFlat(False)
        self.btnWork.setObjectName("btnWork")
        self.horizontalLayout.addWidget(self.btnWork)
        self.btnRelax = QtWidgets.QPushButton(TimeMe)
        self.btnRelax.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnRelax.setObjectName("btnRelax")
        self.horizontalLayout.addWidget(self.btnRelax)
        self.btnPause = QtWidgets.QPushButton(TimeMe)
        self.btnPause.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnPause.setObjectName("btnPause")
        self.horizontalLayout.addWidget(self.btnPause)
        self.btnMenu = QtWidgets.QPushButton(TimeMe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMenu.sizePolicy().hasHeightForWidth())
        self.btnMenu.setSizePolicy(sizePolicy)
        self.btnMenu.setMaximumSize(QtCore.QSize(32, 16777215))
        self.btnMenu.setObjectName("btnMenu")
        self.horizontalLayout.addWidget(self.btnMenu)

        self.retranslateUi(TimeMe)
        QtCore.QMetaObject.connectSlotsByName(TimeMe)

    def retranslateUi(self, TimeMe):
        _translate = QtCore.QCoreApplication.translate
        TimeMe.setWindowTitle(_translate("TimeMe", "TimeMe"))
        self.btnWork.setText(_translate("TimeMe", "Work"))
        self.btnRelax.setText(_translate("TimeMe", "Relax"))
        self.btnPause.setText(_translate("TimeMe", "Pause"))
        self.btnMenu.setText(_translate("TimeMe", "..."))

