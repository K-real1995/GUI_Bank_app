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
        my_db = data_base.Data_base()
        my_db.get_transfer_in_db(self.__name1, self.__name2, int(self.__sum))
