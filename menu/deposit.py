import data_base


class Desosit:

    def __init__(self, name="", sum=0):
        self.__name = name
        self.__sum = sum

    def set_arguments(self, name, sum):
        self.__name = name
        self.__sum = sum

    def make_deposit(self):
        if data_base.db.get(self.__name) is None:
            data_base.db[self.__name] = 0
            data_base.db[self.__name] += int(self.__sum)
        else:
            data_base.db[self.__name] += int(self.__sum)
