import data_base


class Withdraw:
    def __init__(self, name="", sum=0):
        self.__name = name
        self.__sum = sum

    def set_arguments(self, name, sum):
        self.__name = name
        self.__sum = sum

    def get_withdraw(self):
        my_db = data_base.Data_base()
        my_db.make_withdraw_in_db(self.__name, int(self.__sum))
