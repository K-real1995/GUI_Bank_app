from menu import deposit, withdraw, balance, transfer, income


class App_menu:
    def menu(self, arguments_list):
        if arguments_list[0] == "DEPOSIT":
            my_deposit = deposit.Desosit()
            my_deposit.set_arguments(arguments_list[1], arguments_list[2])
            my_deposit.make_deposit()
        elif arguments_list[0] == "WITHDRAW":
            my_withdraw = withdraw.Withdraw()
            my_withdraw.set_arguments(arguments_list[1], arguments_list[2])
            my_withdraw.get_withdraw()
        elif arguments_list[0] == "BALANCE":
            my_balance = balance.Balance()
            try:
                my_balance.set_name(arguments_list[1])
            except:
                my_balance.set_name("Не задано")
            my_balance.get_balance()
        elif arguments_list[0] == "TRANSFER":
            my_trasfer = transfer.Transfer()
            my_trasfer.set_arguments(arguments_list[1], arguments_list[2], arguments_list[3])
            my_trasfer.get_transfer()
        elif arguments_list[0] == "INCOME":
            my_income = income.Income()
            my_income.set_percent(arguments_list[1])
            my_income.set_percent_for_all_accounts()
        else:
            print("Вы ввели неверные значения попробуйте еще раз")
