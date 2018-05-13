# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
from task import Task
import sys
import inspect


class Normal4(Task):

    @staticmethod
    def ask_params():
        my_list = []
        while True:
            n = input(f'Число списка (пусто чтобы закончить): ')
            if n == '':
                break
            my_list.append(n)
        return {'list': my_list}

    def _resolve(self):
        my_list = self.params['list']
        my_set = set(my_list)
        list_unique1 = list(my_set)
        list_unique2 = []
        for el in my_list:
            if my_list.count(el) == 1:
                list_unique2.append(el)
        return f"a) {str(list_unique1)}\nb) {str(list_unique2)}"


if __name__ == "__main__":
    module_classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for cls in module_classes:
        if cls[0] != 'Task':
            Do = cls[1]
            params = Do.ask_params()
            print(Do(params))
            break
