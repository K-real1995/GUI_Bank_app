import json


class Data_base:
    def make_deposit_in_db(self, name, sum):
        with open('customers.json') as f:
            data = json.load(f)

        new_customer = [{"name": name, "sum": sum}]

        buffer = False

        for key in data["customers"]:
            if key["name"] == name:
                buffer = True
                key["sum"] += sum
        if buffer is False:
            data["customers"] += new_customer

        with open('customers.json', 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def make_withdraw_in_db(self, name, sum):
        with open('customers.json') as f:
            data = json.load(f)

        new_customer = [{"name": name, "sum": 0 - sum}]

        buffer = False

        for key in data["customers"]:
            if key["name"] == name:
                buffer = True
                key["sum"] -= sum
        if buffer is False:
            data["customers"] += new_customer

        with open('customers.json', 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def get_balance_in_db(self, name):
        with open('customers.json') as f:
            data = json.load(f)

        buffer = False

        if name == "Не задано":
            for key in data["customers"]:
                print("Клиент: " + key["name"] + ", Баланс: " + str(key["sum"]))

        else:
            for key in data["customers"]:
                if key["name"] == name:
                    print("Баланс клиента " + key["name"] + " равен: " + str(key["sum"]))
                    buffer = True
                    break
            if buffer is False:
                print("NO CLIENT")

    def get_transfer_in_db(self, name1, name2, sum):
        with open('customers.json') as f:
            data = json.load(f)

        buffer1 = False
        for key1 in data["customers"]:
            if key1["name"] == name1:
                key1["sum"] -= sum
                buffer1 = True
                break

        if buffer1 is False:
            new_customer = [{"name": name1, "sum": 0 - sum}]
            data["customers"] += new_customer

        buffer2 = False

        for key2 in data["customers"]:
            if key2["name"] == name2:
                key2["sum"] += sum
                buffer2 = True
                break

        if buffer2 is False:
            new_customer = [{"name": name2, "sum": sum}]
            data["customers"] += new_customer

        with open('customers.json', 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def set_percent_for_all_accounts_in_db(self, percent):
        with open('customers.json') as f:
            data = json.load(f)

        for key in data["customers"]:
            if key["sum"] > 0:
                res = key["sum"] + (key["sum"] / 100 * float(percent))
                key["sum"] = round(res)
            else:
                pass

        with open('customers.json', 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
