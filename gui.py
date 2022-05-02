import sys
from PyQt5 import QtCore, QtGui, QtWidgets

import app_menu
from design import *


class Gui(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_Bank_app()
        self.ui.setupUi(self)
        self.centerOnScreen()
        self.ui.pushButton.clicked.connect(self.input_data)
        self.ui.pushButton_2.clicked.connect(self.output_data)

    # Функция выравнивания окна по центру
    def centerOnScreen(self):
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.move(int(resolution.width() / 2) - int(self.frameSize().width() / 2),
                  int(resolution.height() / 2) - int(self.frameSize().height() / 2))

    def input_data(self):
        text = self.ui.textEdit.toPlainText()
        with open('buffer.txt', "w") as file:
            file.write(text)
        comand_list = []
        with open('buffer.txt', 'r') as file:
            for n, line in enumerate(file, 1):
                line = line.rstrip('\n')
                comand_list.append(line.split())
        for i in comand_list:
            app_menu.App_menu().menu(i)

    def output_data(self):
        a = "SOME TEXT"
        self.ui.textEdit_2.append(a)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Gui()
    window.show()
    sys.exit(app.exec_())
