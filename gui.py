import json
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from design import *


class Gui(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_Bank_app()
        self.ui.setupUi(self)
        self.centerOnScreen()
        self.ui.pushButton.clicked.connect(self.start)
        self.ui.pushButton_2.clicked.connect(self.clear_text_edit)

    # Функция выравнивания окна по центру
    def centerOnScreen(self):
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.move(int(resolution.width() / 2) - int(self.frameSize().width() / 2),
                  int(resolution.height() / 2) - int(self.frameSize().height() / 2))

    # Функция выполнения команд в зависимости от передаваемых параметров
    def execute_comands(self, arguments_list):
        try:
            if arguments_list[0] == "DEPOSIT":
                self.make_deposit_in_db(arguments_list[1], arguments_list[2])
            elif arguments_list[0] == "WITHDRAW":
                self.make_withdraw_in_db(arguments_list[1], arguments_list[2])
            elif arguments_list[0] == "BALANCE":
                try:
                    self.get_balance_in_db(arguments_list[1])
                except IndexError:
                    self.get_balance_in_db("Не задано")
            elif arguments_list[0] == "TRANSFER":
                self.get_transfer_in_db(arguments_list[1], arguments_list[2], arguments_list[3])
            elif arguments_list[0] == "INCOME":
                self.set_percent_for_all_accounts_in_db(arguments_list[1])
            else:
                self.get_error()
        except IndexError:
            pass

    # Функция очищающая оба окна, вызываемая при нажатии кнопки "Clear"
    def clear_text_edit(self):
        self.ui.textEdit_2.clear()
        self.ui.textEdit.clear()

    # Функция вызываемая при нажатии кнопки "Calculate", записывающая аргументы передаваемые в окне № 1 и передающая
    # аргументы в функцию execute_comands
    def start(self):
        self.ui.textEdit_2.clear()
        text = self.ui.textEdit.toPlainText()
        f = open('buffer.txt', "w")
        f.write(text)
        f.close()

        comand_list = []

        file = open('buffer.txt', 'r+')
        for n, line in enumerate(file, 1):
            if len(comand_list) >= 20:
                break
            else:
                line = line.rstrip('\n')
                comand_list.append(line.split())
        for i in comand_list:
            self.execute_comands(i)
        file.close()

    # Функция вызываемая при ошибочном вводе команд
    def get_error(self):
        self.ui.textEdit_2.append("Вы ввели неверные значения попробуйте еще раз")

    # Функция формирующая депозит в базе данных, вызываемая командой: "DEPOSIT" в окне № 1
    def make_deposit_in_db(self, name, sum):
        with open('customers.json') as f:
            data = json.load(f)

        new_customer = [{"name": name, "sum": sum}]

        buffer = False

        for key in data["customers"]:
            if key["name"] == name:
                buffer = True
                key["sum"] += int(sum)
        if buffer is False:
            data["customers"] += new_customer

        with open('customers.json', 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    ##Функция снимающая деньги со счета клиента, вызываемая командой: "WITHDRAW" в окне № 1
    def make_withdraw_in_db(self, name, sum):
        with open('customers.json') as f:
            data = json.load(f)

        new_customer = [{"name": name, "sum": 0 - int(sum)}]

        buffer = False

        for key in data["customers"]:
            if key["name"] == name:
                buffer = True
                key["sum"] -= int(sum)
        if buffer is False:
            data["customers"] += new_customer

        with open('customers.json', 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    # Функция вызывающая баланс клиента, вызывается командой "BALANCE" в окне № 1
    def get_balance_in_db(self, name):
        with open('customers.json') as f:
            data = json.load(f)

        buffer = False

        if name == "Не задано":
            for key in data["customers"]:
                self.ui.textEdit_2.append("Клиент: " + key["name"] + ", Баланс: " + str(key["sum"]))

        else:
            for key in data["customers"]:
                if key["name"] == name:
                    self.ui.textEdit_2.append("Баланс клиента " + key["name"] + " равен: " + str(key["sum"]))
                    buffer = True
                    break
            if buffer is False:
                self.ui.textEdit_2.append("NO CLIENT")

    # Функция перевода денежных средств от одного клиента к другому, вызываемая командой "TRANSFER" в окне № 1
    def get_transfer_in_db(self, name1, name2, sum):
        with open('customers.json') as f:
            data = json.load(f)

        buffer1 = False
        for key1 in data["customers"]:
            if key1["name"] == name1:
                key1["sum"] -= int(sum)
                buffer1 = True
                break

        if buffer1 is False:
            new_customer = [{"name": name1, "sum": 0 - sum}]
            data["customers"] += new_customer

        buffer2 = False

        for key2 in data["customers"]:
            if key2["name"] == name2:
                key2["sum"] += int(sum)
                buffer2 = True
                break

        if buffer2 is False:
            new_customer = [{"name": name2, "sum": sum}]
            data["customers"] += new_customer

        with open('customers.json', 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    # Функция прибавляющая всем клиентам заданное количество процентов, вызываемая кмандой "INCOME" в окне № 1
    def set_percent_for_all_accounts_in_db(self, percent):
        with open('customers.json') as f:
            data = json.load(f)

        for key in data["customers"]:
            if key["sum"] > 0:
                res = key["sum"] + (key["sum"] / 100 * float(percent))
                key["sum"] = round(res)
            else:
                pass

        with open('customers.json', 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Gui()
    window.show()
    sys.exit(app.exec_())
