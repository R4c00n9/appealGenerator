# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_aboutForm(object):
    def setupUi(self, aboutForm):
        aboutForm.setObjectName("aboutForm")
        aboutForm.resize(248, 100)
        self.dntBtn = QtWidgets.QPushButton(aboutForm)
        self.dntBtn.setGeometry(QtCore.QRect(10, 10, 231, 23))
        self.dntBtn.setObjectName("dntBtn")
        self.back2mainBtn = QtWidgets.QPushButton(aboutForm)
        self.back2mainBtn.setGeometry(QtCore.QRect(10, 70, 231, 23))
        self.back2mainBtn.setObjectName("back2mainBtn")
        self.dntBtn2 = QtWidgets.QPushButton(aboutForm)
        self.dntBtn2.setGeometry(QtCore.QRect(10, 40, 231, 23))
        self.dntBtn2.setMinimumSize(QtCore.QSize(231, 23))
        self.dntBtn2.setMaximumSize(QtCore.QSize(231, 23))
        self.dntBtn2.setObjectName("dntBtn2")

        self.retranslateUi(aboutForm)
        QtCore.QMetaObject.connectSlotsByName(aboutForm)

    def retranslateUi(self, aboutForm):
        _translate = QtCore.QCoreApplication.translate
        aboutForm.setWindowTitle(_translate("aboutForm", "About"))
        self.dntBtn.setText(_translate("aboutForm", "Creator"))
        self.back2mainBtn.setText(_translate("aboutForm", "Back"))
        self.dntBtn2.setText(_translate("aboutForm", "Supporter"))


