# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
from task import Task
import sys
import inspect
import random


class Normal3(Task):

    @staticmethod
    def ask_params():
        n = int(input('Введите n: '))
        return {'n': n}

    def _resolve(self):
        n = self.params['n']
        my_list = []
        for i in range(n):
            my_list.append(random.randint(-100, 100))
        return str(my_list)


if __name__ == "__main__":
    module_classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for cls in module_classes:
        if cls[0] != 'Task':
            Do = cls[1]
            params = Do.ask_params()
            print(Do(params))
            break
