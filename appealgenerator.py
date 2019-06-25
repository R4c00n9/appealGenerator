import sys
import webbrowser

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QLineEdit, QTextEdit
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from libs.appealUI import Ui_MainWindow
from libs.aboutUI import Ui_aboutForm
from libs.mainUI import Ui_mainDialog #Импортируем все нужное


class aboutWindow(QtWidgets.QMainWindow, Ui_aboutForm):  #Создаем класс для окна About
    def __init__(self, parent=None):
        super(aboutWindow, self).__init__()

        self.setupUi(self)

        self.back2mainBtn.clicked.connect(self.close)
        self.dntBtn.clicked.connect(lambda: webbrowser.open('https://vk.com/minusls', new=1)) #Ссылка на -LS
        self.dntBtn2.clicked.connect(lambda: webbrowser.open('https://vk.com/wh1ten2ght', new=1)) #Ссылка на nightness3


class greetingsWindow(QtWidgets.QMainWindow, Ui_MainWindow):  #Создаем класс для начального окна greetings
    def __init__(self, parent=None):
        super(greetingsWindow, self).__init__()

        self.setupUi(self)

        self.exitBtn.clicked.connect(self.close) #кнопка exit
        self.nextBtn.clicked.connect(self.ChangeWindows1) #кнопка next
        self.dialog1 = generatorWindow(self)

        self.aboutBtn.clicked.connect(self.ChangeWindows) #кнопка About
        self.dialog = aboutWindow(self)

    def closeEvent(self, event): #начало event exit
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore() #конец event exit

    def ChangeWindows(self):
        self.dialog.show()

    def ChangeWindows1(self):
        self.dialog1.show()

class generatorWindow(QtWidgets.QMainWindow, Ui_mainDialog): #создаем class для окна generator
    def __init__(self, parent=None):
        super(generatorWindow, self).__init__()
        self.setupUi(self)

        self.exitBtn.clicked.connect(self.close) #кнопка exit
        self.pushButton.clicked.connect(self.generate) #кнопка generate

    def closeEvent(self, event): #снова event exit
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore() #конец event exit

    def generate(self): #снимаем значения с строк
        nick = self.nameEdit.text()
        multi = str(self.multiList.toPlainText())
        cheat = str(self.cheatList.toPlainText()) 
        insult = str(self.insultList.toPlainText())
        smth = str(self.smthList.toPlainText()) #конец снятия значения с строк

        #Дописать проверку на наполненность каждого TextEdit, если контента в TextEdit нет,
        #то отключить генерацию этого модуля.



def main():
    app = QApplication(sys.argv)
    GW = greetingsWindow()
    GW.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
