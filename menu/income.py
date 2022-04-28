import data_base


class Income:
    def __init__(self, percent=0):
        self.__percent = percent

    def set_percent(self, percent):
        self.__percent = percent
        for key, value in data_base.db.items():
            if value <= 0:
                pass
            else:
                res = value + (value / 100 * float(percent))
                data_base.db[key] = round(res)


