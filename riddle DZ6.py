
"""
1. Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками.
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.
"""
def riddle (mist: str, res:list, chance: int) -> int:
    print(mist)
    for i in range(chance):
        ch = input(f'введите ответ ')
        if ch in res:
            print('Правильно!')
            return i + 1
    return 0

def _list_riddle (a:list, b:list):
    gen_riddle = {key: value for key in mist_list for value in res_list}
    print(gen_riddle)
    return gen_riddle


mist_list = ['Зимой и летом одним цветом', "Ни лает, ни кусает, а в дом не пускает"]
res_list = [['Елочка', 'Ель', 'Елка'], ['Замок', 'замок', 'ЗАМОК']]

def nigma (:dict):
    for key in dict:
        return key


print(nigma(gen_riddle))

if __name__ == '__main__':

    mist = 'Зимой и летом одним цветом!'
    res = ['Елочка', 'Ель', 'Елка']


    print(list_riddle(mist_list, res_list))
    print(riddle(mist, res, 4))