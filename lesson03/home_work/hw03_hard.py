# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3
from fraction import Fraction


def calc_fractions(str_):
    print(f'Вычисляем {str_}')
    if str_.find(' + ') > 0:
        arguments = str_.split(' + ')
        result = Fraction(arguments[0]) + Fraction(arguments[1])
        print(f'Результат: {result}\n')
    elif str_.find(' - ') > 0:
        arguments = str_.split(' - ')
        result = Fraction(arguments[0]) - Fraction(arguments[1])
        print(f'Результат: {result}\n')
    else:
        print('Не удалось определить операцию\n')


calc_fractions('5/6 + 4/7')
calc_fractions('1/6 + 1/3')
calc_fractions('-2/3 - -2')
calc_fractions('-1 1/6 - -2/3')
calc_fractions('-1 1/6 + 3 2/12')

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


with open('data/workers', encoding='utf-8') as f:
    lines = f.readlines()[1:]
workers = {}
for l in lines:
    ls = l.split()
    workers.update({f'{ls[0]} {ls[1]}': {'salary': int(ls[2]), 'norm': int(ls[4]), 'hours': None}})

with open('data/hours_of', encoding='utf-8') as f:
    lines = f.readlines()[1:]
for l in lines:
    ls = l.split()
    workers[f'{ls[0]} {ls[1]}']['hours'] = int(ls[2])

for name, sums in workers.items():
    if not sums['hours']:
        print(f'{name} не работал')
    else:
        if sums['norm'] < sums['hours']:
            salary = sums['salary'] * (1 + (2 / sums['norm']) * (sums['hours'] - sums['norm']))
        else:
            salary = sums['salary'] * (sums['hours'] / sums['norm'])
        salary = round(salary, 2)
        print(f'{name} заработал {salary}')


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

rng = range(ord('А'), ord('Я')+1)
letters = dict(zip(list(map(chr, rng)), [[] for _ in rng]))
with open("data/fruits.txt", encoding='utf-8') as f:
    lines = f.readlines()
for l in lines:
    v = l.strip()
    if v == '':
        continue
    first_letter = v[0].upper()
    letters[first_letter].append(v)

for letter, content in letters.items():
    with open(f"data/fruits_{letter}.txt", 'w', encoding='utf-8') as f:
        f.writelines(map(lambda x: x+'\n', content))
