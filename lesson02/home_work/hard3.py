# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

"""
Функция вычисляет номер квадрата из комнат (1+2**2+3**2+4**2...) в котором наше число
Номер первого этажа в этом квадрата
Номер первой комнаты в квадрате
"""

from task import Task
import sys, inspect


class Hard3(Task):
    max_iter = 2000

    @staticmethod
    def ask_params():
        number = int(input('Введите номер комнаты: '))
        return {'N': number}

    def _calculate_block(self):
        block = 0
        last_room = 0
        last_floor = 0
        while True:
            block += 1
            last_room += block ** 2
            last_floor += block
            if self.number <= last_room:
                first_room = last_room - block ** 2 + 1
                first_floor = last_floor - block + 1
                return block, first_floor, first_room
            if block > self.max_iter:
                print("Решение не найдено")
                break

    def _calculate_floor(self, block, first_floor, first_room):
        shift = self.number - first_room
        floor = first_floor + shift // block
        room = shift % block + 1
        return floor, room

    def _resolve(self):
        self.number = self.params['N']
        block_number, first_floor_in_block, first_room_in_block = self._calculate_block()
        floor_of_room, room_on_floor = self._calculate_floor(block_number, first_floor_in_block, first_room_in_block)
        return f'Номер этажа = {floor_of_room}, Номер команты на этаже = {room_on_floor}'



if __name__ == "__main__":
    module_classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for cls in module_classes:
        if cls[0] != 'Task':
            Do = cls[1]
            params = Do.ask_params()
            print(Do(params))
            break
