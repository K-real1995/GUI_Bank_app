import data_base


class Income:
    def __init__(self, percent=0):
        self.__percent = percent

    def set_percent(self, percent):
        self.__percent = percent

    def set_percent_for_all_accounts(self):
        my_db = data_base.Data_base()
        my_db.set_percent_for_all_accounts_in_db(int(self.__percent))
