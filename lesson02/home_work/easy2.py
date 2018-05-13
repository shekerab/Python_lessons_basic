# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
from task import Task
import sys, inspect


class Easy2(Task):

    @staticmethod
    def ask_params():
        my_lists = [[],[]]
        for i in range(2):
            while True:
                n = input(f'Список {i+1}:число (пусто чтобы закончить): ')
                if n == '':
                    break
                my_lists[i].append(n)
        return {'lists': my_lists}

    def _resolve(self):
        lists = self.params['lists']
        lists[0] = list(set(lists[0]) - set(lists[1]))
        return str(lists[0])


if __name__ == "__main__":
    module_classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for cls in module_classes:
        if cls[0] != 'Task':
            Do = cls[1]
            params = Do.ask_params()
            print(Do(params))
            break
