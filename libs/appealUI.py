# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appealUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(635, 180)
        MainWindow.setMinimumSize(QtCore.QSize(635, 180))
        MainWindow.setMaximumSize(QtCore.QSize(635, 180))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.mainWgt = QtWidgets.QWidget(MainWindow)
        self.mainWgt.setObjectName("mainWgt")
        self.exitBtn = QtWidgets.QPushButton(self.mainWgt)
        self.exitBtn.setGeometry(QtCore.QRect(560, 150, 71, 23))
        self.exitBtn.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.exitBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.exitBtn.setObjectName("exitBtn")
        self.nextBtn = QtWidgets.QPushButton(self.mainWgt)
        self.nextBtn.setGeometry(QtCore.QRect(460, 150, 71, 23))
        self.nextBtn.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.nextBtn.setObjectName("nextBtn")
        self.aboutBtn = QtWidgets.QPushButton(self.mainWgt)
        self.aboutBtn.setGeometry(QtCore.QRect(10, 150, 75, 23))
        self.aboutBtn.setObjectName("aboutBtn")
        self.infLbl = QtWidgets.QLabel(self.mainWgt)
        self.infLbl.setGeometry(QtCore.QRect(10, 20, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.infLbl.setFont(font)
        self.infLbl.setObjectName("infLbl")
        self.infLbl2 = QtWidgets.QLabel(self.mainWgt)
        self.infLbl2.setGeometry(QtCore.QRect(10, 50, 611, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.infLbl2.setFont(font)
        self.infLbl2.setTextFormat(QtCore.Qt.PlainText)
        self.infLbl2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.infLbl2.setObjectName("infLbl2")
        MainWindow.setCentralWidget(self.mainWgt)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Greetings!"))
        self.exitBtn.setText(_translate("MainWindow", "Exit"))
        self.nextBtn.setText(_translate("MainWindow", "Next"))
        self.aboutBtn.setText(_translate("MainWindow", "About"))
        self.infLbl.setText(_translate("MainWindow", "Greetings!"))
        self.infLbl2.setText(_translate("MainWindow", "Hello! You downloaded appeal generator. There\'s not much time left before you can write your \n"
"message to osu support. All you need is information about the reason for the ban, as well as \n"
"exhaustive evidence that you will now become an exemplary player. After generating the \n"
"appeal, it is stored in a textfile from which you can safely copy it.All you have to do is click on \n"
"Next. Good luck! And if you want to help the creators or learn more about them - click"))


