import data_base


class Desosit:

    def __init__(self, name="", sum=0):
        self.__name = name
        self.__sum = sum

    def set_arguments(self, name, sum):
        self.__name = name
        self.__sum = sum

    def make_deposit(self):
        my_db = data_base.Data_base()
        my_db.make_deposit_in_db(self.__name, int(self.__sum))
