import data_base


class Withdraw:
    def __init__(self, name="", sum=0):
        self.__name = name
        self.__sum = sum

    def set_arguments(self, name, sum):
        self.__name = name
        self.__sum = sum

    def get_withdraw(self):
        if data_base.db.get(self.__name) is None:
            data_base.db[self.__name] = 0
            data_base.db[self.__name] -= int(self.__sum)
        else:
            data_base.db[self.__name] -= int(self.__sum)
