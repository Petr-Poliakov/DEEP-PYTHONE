"""
Напишите функцию для транспонирования матрицы
"""
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def trans_matr (a) -> list:
    """транспортирование матрицы 3 Х 3"""
    b = list()
    for item in zip(*a):
        b.append(item)
    print(b[0], '\n', b[1], '\n', b[2],'\n')
    return b

print(a[0], '\n', a[1], '\n', a[2])
print()
trans_matr(a)

"""
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ - значение переданного
аргумента, а значение - имя аргумента. Если ключ не хешируем, используйте его строковое представление.
"""
def my_key(**kwargs) -> dict:
    for key, value in kwargs.items():
        # print(value)
        dict = {value: key}
        print(dict)

my_key(a=4334, b=31231, c=3)
print()
"""
*Доп задача *
Задачу о банкомате
Разбейте её на отдельные операции - функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.
Начальная сумма равна нулю - DONE
Допустимые действия: пополнить, снять, выйти
Сумма пополнения и снятия кратны 50 у.е. - DONE
Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е. - DONE
После каждой третей операции пополнения или снятия начисляются проценты - 3% - DONE
Нельзя снять больше, чем на счёте - DONE
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной - DONE
Любое действие выводит сумму денег
"""
balance = int(0)
log_list = list()

def input_cash(a: int): #-> balance:
    global balance
    global log_list
    global procent
    if balance > 5000000:
        RICH_Nalog = float(balance * 0.10)
        balance = balance - RICH_Nalog
        print(f'с Вас удержан налог на богатство в размере 10% {RICH_Nalog} на счете доступно {balance}')

    if a >= 50:
        balance += a
        print(f'Пополнение счета на {a}')
        print(f'на вашем счету {balance}')

        log_list.append("+")  # коунт для логирования количества операций, 3%
        if log_list.count("+") == 3:
            procent = balance * 0.03
            balance = balance + procent
            print(f'Вам начислен процент на остаток суммы 3% остаток на счете {balance} y.e.')
            log_list = list()
        else:
            None
        return balance
    else:
        print('минимальная сумма пополнения 50 у.е')


def out_cash(b: int) -> balance:
    global balance
    global log_list
    global procent
    if balance > 5000000:
        RICH_Nalog = float(balance * 0.10)
        balance = balance - RICH_Nalog
        print(f'с Вас удержан налог на богатство в размере 10% {RICH_Nalog} на счете доступно {balance}')

    if b > balance or b < 50:
        print('недостаточно средств на счете')
    else:
        MIN_COMIS = 30
        MAX_COMIS = 600
        comis = 1.5*b/100
        if 30 < comis < 600:
            balance = balance - (b + comis)
            print(f'Выдача наличных {b} y.e, остаток на счете {balance}')
            print(f'Комиссия за снятие составляет , {comis}')
        elif comis < 30:
            balance = balance - (b + MIN_COMIS)
            print(f'Выдача наличных {b} y.e, остаток на счете {balance}')
            print(f'Комиссия за снятие составляет ,{MIN_COMIS}')
        else:
            balance = balance - (b + MAX_COMIS)
            print(f'Выдача наличных {b} y.e, остаток на счете {balance}')
            print(f'Комиссия за снятие составляет ,{MAX_COMIS}')

        log_list.append("-") # коунт для логирования количества операций, 3%
        if log_list.count("-") == 3:
            procent = balance * 0.03
            balance = balance + procent
            print(f'Вам начислен процент на остаток суммы 3% остаток на счете {balance} y.e.')
            log_list = list()
        else:
            None


print(log_list)
input_cash(150000000)
out_cash(3000000)
out_cash(500000)
out_cash(140000000)
print(log_list)
input_cash(300)
print(log_list)

input_cash(30)
input_cash(10000000)