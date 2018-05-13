# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
# date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'
from task import Task
from normal2 import Normal2
import sys
import inspect


class Hard1(Task):
    max_iter = 2000

    @staticmethod
    def ask_params():
        my_date = input('Введите дату: ')
        return {'date': my_date}

    def _resolve(self):
        my_date = self.params['date']
        date_parts = my_date.split('.')
        result = len(date_parts) == 3
        result = result and len(date_parts[0]) == 2 and len(date_parts[1]) == 2 and len(date_parts[2]) == 4
        result = result and date_parts[0].isdigit() and date_parts[1].isdigit() and date_parts[2].isdigit()
        if result:
            d = int(date_parts[0])
            m = int(date_parts[1])
            y = int(date_parts[2])
            result = m in (1, 4, 6, 9, 11) and d in range(1,31) \
                             or m == 2 and d in range(1,30) and y % 4 == 0 and (y % 100 != 0 or y % 400 == 0) \
                             or m == 2 and d in range(1,29) and (y % 4 != 0 or y % 100 == 0 and y % 400 != 0) \
                             or m in (3, 5, 7, 8, 10, 12) and d in range(1, 32)
        else:
            return f"Не корректный формат даты"
        if result:
            in_rus = Normal2({'date': my_date})
            return f"Дата корректная: {in_rus}"
        else:
            return f"Не существующая дата"

if __name__ == "__main__":
    module_classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for cls in module_classes:
        if cls[0] != 'Task':
            Do = cls[1]
            params = Do.ask_params()
            print(Do(params))
            break
