"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""

my_str = "/Users/petrpolakov/Documents/Deep_Python/venv/lesson5/DZ5.py"

def str_back_tuple(n:str)-> tuple:
    *way, exp = n.split('/')
    name_file, final_exp = exp.split('.', 2)
    print(f'{way = },{name_file = }, {final_exp = }')
    return

str_back_tuple(my_str)
"""
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, 
ставка int, премия str с указанием процентов вида “10.25%”.
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
Сумма рассчитывается как ставка умноженная на процент премии
"""
list_name = ('Pavel', 'Sergey', 'Nikita', 'Alex')
list_bet = (100, 200, 500, 5)
list_prize = ('10.25%', '15.00%', '5.90%', '13%')

my_gen = {key: value1 * value2 for key in list_name for value1 in list_bet for value2 in list_prize}
print(my_gen)
"""
Создайте функцию генератор чисел Фибоначчи (см. Википедию)
"""
def fibonachi (n):
    if n <= 1:
        yield n
    else:
        dig = 0
        fib_magic = 1
        for i in range(1, n+1):
            sum_fib = dig + fib_magic
            dig = fib_magic
            fib_magic = sum_fib
            # print(f' шаг {i}, {sum_fib}')
        yield sum_fib

print(*fibonachi(10))
