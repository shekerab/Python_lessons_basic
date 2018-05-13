# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
from task import Task
import sys
import inspect
import math


class Normal1(Task):

    @staticmethod
    def ask_params():
        my_list = []
        while True:
            n = input('Число (пусто чтобы закончить): ')
            if n == '':
                break
            my_list.append(int(n))
        return {'list': my_list}

    def _resolve(self):
        my_list = self.params['list']
        res_list = []
        for el in my_list:
            if el >= 0:
                sqr = math.sqrt(el)
                if sqr.is_integer():
                    res_list.append(int(sqr))
        return str(res_list)


if __name__ == "__main__":
    module_classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for cls in module_classes:
        if cls[0] != 'Task':
            Do = cls[1]
            params = Do.ask_params()
            print(Do(params))
            break
