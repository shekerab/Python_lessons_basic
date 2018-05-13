# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
# equation = 'y = -12x + 11111140.2121'
# x = 2.5
# вычислите и выведите y

from task import Task
import sys
import inspect


class Hard1(Task):

    @staticmethod
    def ask_params():
        equation = input('Введите уравнение: ')
        x = float(input('Введите значение x: '))
        return {'equation': equation, 'x': x}

    def _resolve(self):
        equation = self.params['equation']
        x = self.params['x']
        equation = equation.split('=')[1].strip()
        equation = equation.replace('x', '')
        ab = equation.split('+')
        a = float(ab[0].strip())
        b = float(ab[1].strip())
        return f'result = {a * x + b}'


if __name__ == "__main__":
    module_classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for cls in module_classes:
        if cls[0] != 'Task':
            Do = cls[1]
            params = Do.ask_params()
            print(Do(params))
            break
