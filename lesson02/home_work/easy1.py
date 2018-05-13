# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
# Подсказка: воспользоваться методом .format()
from task import Task
import sys
import inspect


class Easy1(Task):

    @staticmethod
    def ask_params():
        fruits = []
        while True:
            fruit = input('Введите фрукт(пустой чтобы закончить): ')
            if fruit == '':
                break
            fruits.append(fruit)
        return {'fruits': fruits}

    def _resolve(self):
        fruits = self.params['fruits']
        res_str = ''
        max_len = len(max(fruits, key=len))
        for i, fruit in enumerate(fruits,1):
            res_str += '{i}. {fruit:>{shift}}\n'.format(i=i,fruit=fruit, shift=max_len)
        return res_str


if __name__ == "__main__":
    module_classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for cls in module_classes:
        if cls[0] != 'Task':
            Do = cls[1]
            params = Do.ask_params()
            print(Do(params))
            break
