# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
from task import Task
import sys
import inspect


class Easy3(Task):

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
            if el % 2 == 0:
                res_list.append(el/4)
            else:
                res_list.append(el*2)
        return str(res_list)


if __name__ == "__main__":
    module_classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for cls in module_classes:
        if cls[0] != 'Task':
            Do = cls[1]
            params = Do.ask_params()
            print(Do(params))
            break
