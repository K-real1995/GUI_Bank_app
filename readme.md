ПРОГРАММА ОБРАБАТЫВАЕТ ТЕКСТОВЫЕ КОМАНДЫ
ИЗ ЛЕВОГО ПОЛЯ ТОЛЬКО ПОСЛЕ НАЖАТИЯ КНОПКИ «Calculate».
То есть, пользователь СНАЧАЛА вводит желаемые команды, при этом
каждая новая команда вводится с новой строки, а ПОТОМ нажимает на
кнопку «Calculate». Результат должен быть выведен в поле справа.
Количество команд, которые может ввести пользователь за один раз – не
более 20. При необходимости следует предусмотреть прокрутку в поле.
Пользователю допускается вводить «пустые строки» - несколько раз
нажимать на кнопку «enter». При нажатии клавиши ввода «enter», фокус
не должен переходить на кнопку «Calculate».

1.Команды вводятся пользователем только большими буквами. Сама команда, имя клиента, суммы (числа) разделяются пробелами.

2Предполагается, что пользователь такой системы грамотный и команды с аргументами вводит без ошибок в рамках их вышесформулированного синтаксиса.

3.Как только для несуществующего ранее клиента проводится операция
пополнения (DEPOSIT), снятия (WITHDRAW) или перевода денег
(TRANSFER), он вносится в систему, ему заводится счет с указанным
балансом. Все дальнейшие операции проводятся только с этим счетом.
Сумма на счету может быть как положительной, так и отрицательной,
при этом всегда является целым числом.

Список команд:
1. DEPOSIT name sum. Зачислить сумму sum на счет клиента
name. Если клиента нет, то он создает-
ся и на него заводится счет с указан-
ной суммой.
2. WITHDRAW name sum. Снять сумму sum со счета клиента
name. Если клиента, то счет создается.
Баланс при выполнении такой опера-
ции у вновь созданного клиента дол-
жен быть отрицательный.
3. BALANCE name. Узнать остаток средств на счету кли-
ента name. Для каждого запроса
BALANCE программа должна вывести
остаток на счету данного клиента. Ес-
ли же у клиента с запрашиваемым
именем не открыт счет в банке, выво-
дится сообщение «NO CLIENT». Если
пользователь не указал имя клиента –
то выводится баланс всех существую-
щих клиентов.
4. TRANSFER name1 name2
sum. Перевести сумму sum со счета клиента
name1 на счет клиента name2. Если у
какого-либо клиента, то он заводится в
системе и ему создается счет с переве-15
денной суммой.
5. INCOME p.
Начислить всем клиентам, у которых
открыты счета, p% от суммы счета.
Проценты начисляются только клиен-
там с положительным остатком на сче-
ту, если у клиента остаток отрицатель-
ный, то его счет не меняется. После
начисления процентов сумма на счету
остается целой, то есть начисляется
только целое число денежных единиц.
Дробная часть начисленных процентов
отбрасывается.