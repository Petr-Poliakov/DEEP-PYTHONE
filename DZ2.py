#Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое
# представление. Функцию hex используйте для проверки своего результата.
d = int(input ('Введите целое число '))
s = d
res_hex = ''
result = ''
HEX = 16
print(hex(d))
while d > 0:
    res_hex = d % HEX
    result = str(res_hex)+result
    d = d//HEX
print(result)
import fractions
# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
a = (str(input(f'введите числитель и знаменатель через знак "/" ')))
b = (str(input('введите числитель и знаменатель через знак "/" ')))
a_fl = float(a.replace('/', '.'))
b_fl = float(b.replace('/', '.'))
summa = a_fl + b_fl
mult = a_fl * b_fl
print(f'Сумма {a} и {b} равна {summa}')
print(f'Произведение {a} и {b} равна {mult}')

f1 = fractions.Fraction(a)
f2 = fractions.Fraction(b)
print(f1 + f2)
print(f1 * f2)

