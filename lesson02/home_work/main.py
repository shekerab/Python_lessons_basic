from hard3 import Hard3
from easy1 import Easy1
from easy2 import Easy2
from easy3 import Easy3
from normal1 import Normal1
from normal2 import Normal2
from normal3 import Normal3
from normal4 import Normal4

tasks = {
    '1': Easy1,
    '2': Easy2,
    '3': Easy3,
    '4': Normal1,
    '5': Normal2,
    '6': Normal3,
    '7': Normal4,
    '10': Hard3
}

hello = """Введите номер задачи (или x для выхода)
1 - Easy 1 (список фруктов)
2 - Easy 2(Разница списков)
3 - Easy 3
4 - Normal 1
5 - Normal 2
6 - Normal 3
7 - Normal 4
8 - Hard 1
9 - Hard 2 
10 - Hard 3 задача про башню
"""

while True:
    print(hello)
    answer = input('Введите номер задачи: ')
    Do = None
    if answer == 'x':
        break
    elif answer in tasks:
        Do = tasks[answer]
    else:
        print("Ответ не распознан")
        continue

    params = Do.ask_params()
    print(Do(params))
