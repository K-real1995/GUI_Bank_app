import data_base


class Balance:
    def __init__(self, name=""):
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_balance(self):
        if self.__name == "Не задано":
            for key, value in data_base.db.items():
                print("Клиент: " + key + ", Баланс: " + str(value))
        elif data_base.db.get(self.__name) is None:
            print("NO CLIENT")
        else:
            print("Баланс клиента " + self.get_name() + " равен: " + str(data_base.db.get(self.__name)))
