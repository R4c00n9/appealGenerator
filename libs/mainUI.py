# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_mainDialog(object):
    def setupUi(self, mainDialog):
        mainDialog.setObjectName("mainDialog")
        mainDialog.resize(421, 402)

        self.nickLbl = QtWidgets.QLabel(mainDialog)
        self.nickLbl.setGeometry(QtCore.QRect(10, 10, 141, 21))

        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)

        self.nickLbl.setFont(font)
        self.nickLbl.setTextFormat(QtCore.Qt.AutoText)
        self.nickLbl.setObjectName("nickLbl")

        self.nameEdit = QtWidgets.QLineEdit(mainDialog)
        self.nameEdit.setGeometry(QtCore.QRect(150, 10, 261, 20))
        self.nameEdit.setObjectName("nameEdit")

        self.multiLbl = QtWidgets.QLabel(mainDialog)
        self.multiLbl.setGeometry(QtCore.QRect(10, 50, 191, 16))

        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)

        self.multiLbl.setFont(font)
        self.multiLbl.setObjectName("multiLbl")

        self.multiList = QtWidgets.QTextEdit(mainDialog)
        self.multiList.setGeometry(QtCore.QRect(190, 40, 221, 51))
        self.multiList.setDocumentTitle("")
        self.multiList.setObjectName("multiList")

        self.cheatLbl = QtWidgets.QLabel(mainDialog)
        self.cheatLbl.setGeometry(QtCore.QRect(10, 120, 181, 21))

        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)

        self.cheatLbl.setFont(font)
        self.cheatLbl.setObjectName("cheatLbl")

        self.cheatList = QtWidgets.QTextEdit(mainDialog)
        self.cheatList.setGeometry(QtCore.QRect(190, 110, 221, 51))
        self.cheatList.setDocumentTitle("")
        self.cheatList.setObjectName("cheatList")

        self.exitBtn = QtWidgets.QPushButton(mainDialog)
        self.exitBtn.setGeometry(QtCore.QRect(10, 342, 171, 51))
        self.exitBtn.setObjectName("exitBtn")

        self.pushButton = QtWidgets.QPushButton(mainDialog)
        self.pushButton.setGeometry(QtCore.QRect(190, 342, 221, 51))
        self.pushButton.setObjectName("pushButton")

        self.insultList = QtWidgets.QTextEdit(mainDialog)
        self.insultList.setGeometry(QtCore.QRect(190, 180, 221, 51))
        self.insultList.setDocumentTitle("")
        self.insultList.setObjectName("insultList")

        self.insultLbl = QtWidgets.QLabel(mainDialog)
        self.insultLbl.setGeometry(QtCore.QRect(10, 190, 181, 21))

        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)

        self.insultLbl.setFont(font)
        self.insultLbl.setObjectName("insultLbl")

        self.smthList = QtWidgets.QTextEdit(mainDialog)
        self.smthList.setGeometry(QtCore.QRect(190, 250, 221, 81))
        self.smthList.setDocumentTitle("")
        self.smthList.setObjectName("smthList")

        self.smthLbl = QtWidgets.QLabel(mainDialog)
        self.smthLbl.setGeometry(QtCore.QRect(10, 280, 181, 21))

        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        
        self.smthLbl.setFont(font)
        self.smthLbl.setObjectName("smthLbl")

        self.retranslateUi(mainDialog)
        QtCore.QMetaObject.connectSlotsByName(mainDialog)

    def retranslateUi(self, mainDialog):
        _translate = QtCore.QCoreApplication.translate
        mainDialog.setWindowTitle(_translate("mainDialog", "Generator"))
        self.nickLbl.setText(_translate("mainDialog", "Your nickname:"))
        self.nameEdit.setText(_translate("mainDialog", "Insert your name here"))
        self.multiLbl.setText(_translate("mainDialog", "Your multiaccounts:"))
        self.multiList.setHtml(_translate("mainDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Write the multiaccounts you used here. If you didn\'t use multiaccounts, erase those words.</span></p></body></html>"))
        self.cheatLbl.setText(_translate("mainDialog", "Cheats you\'ve used:"))
        self.cheatList.setHtml(_translate("mainDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Write the cheats you used here. If you didn\'t use cheats, erase those words.</span></p></body></html>"))
        self.exitBtn.setText(_translate("mainDialog", "Exit"))
        self.pushButton.setText(_translate("mainDialog", "Generate"))
        self.insultList.setHtml(_translate("mainDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Write the insults you used here. If you didn\'t use insults, erase those words.</span></p></body></html>"))
        self.insultLbl.setText(_translate("mainDialog", "Insults you\'ve used:"))
        self.smthList.setHtml(_translate("mainDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Just write here what you want to add to appeal, facts, excuses. If you do not want to add anything, the system itself will add a certain phrase, suitable court.</span></p></body></html>"))
        self.smthLbl.setText(_translate("mainDialog", "Smth what you want add:"))
