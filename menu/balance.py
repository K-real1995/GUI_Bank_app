import data_base


class Balance:
    def __init__(self, name=""):
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_balance(self):
        my_db = data_base.Data_base()
        my_db.get_balance_in_db(self.__name)

