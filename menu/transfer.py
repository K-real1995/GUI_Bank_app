import data_base


class Transfer:
    def __init__(self, name1="", name2="", sum=0):
        self.__name1 = name1
        self.__name2 = name2
        self.__sum = sum

    def set_arguments(self, name1, name2, sum):
        self.__name1 = name1
        self.__name2 = name2
        self.__sum = sum

    def get_transfer(self):
        if data_base.db.get(self.__name2) is None:
            data_base.db[self.__name2] = 0
            data_base.db[self.__name2] += int(self.__sum)
            data_base.db[self.__name1] -= int(self.__sum)
        else:
            data_base.db[self.__name2] += int(self.__sum)
            data_base.db[self.__name1] -= int(self.__sum)

