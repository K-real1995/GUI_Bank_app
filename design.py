from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Bank_app(object):
    def setupUi(self, Bank_app):
        Bank_app.setObjectName("Bank_app")
        Bank_app.setEnabled(True)
        Bank_app.resize(715, 542)
        Bank_app.setStyleSheet("background-color: rgb(19, 5, 144); color:rgb(228,205,254)")
        self.pushButton = QtWidgets.QPushButton(Bank_app)
        self.pushButton.setGeometry(QtCore.QRect(130, 490, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Bank_app)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 490, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(Bank_app)
        self.textEdit.setGeometry(QtCore.QRect(40, 110, 291, 361))
        self.textEdit.setStyleSheet("background-color:rgb(228,205,254); color:rgb(0, 0, 0); font: italic 12pt \"Sans\";")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Bank_app)
        self.textEdit_2.setGeometry(QtCore.QRect(400, 110, 291, 361))
        self.textEdit_2.setMinimumSize(QtCore.QSize(0, 361))
        self.textEdit_2.setMaximumSize(QtCore.QSize(291, 361))
        self.textEdit_2.setStyleSheet("background-color:rgb(228,205,254); color:rgb(0, 0, 0); font: italic 12pt \"Sans\";")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textBrowser = QtWidgets.QTextBrowser(Bank_app)
        self.textBrowser.setGeometry(QtCore.QRect(40, 60, 291, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Bank_app)
        self.textBrowser_2.setGeometry(QtCore.QRect(400, 60, 291, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.retranslateUi(Bank_app)
        QtCore.QMetaObject.connectSlotsByName(Bank_app)

    def retranslateUi(self, Bank_app):
        _translate = QtCore.QCoreApplication.translate
        Bank_app.setWindowTitle(_translate("Bank_app", "Dialog"))
        self.pushButton.setText(_translate("Bank_app", "Calculate"))
        self.pushButton_2.setText(_translate("Bank_app", "Clear"))
        self.textBrowser.setHtml(_translate("Bank_app", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Input window</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Bank_app", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Output window</span></p></body></html>"))
