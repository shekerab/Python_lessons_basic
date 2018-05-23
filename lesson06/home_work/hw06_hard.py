# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

class Worker:
    def __init__(self, init_str):
        ls = init_str.split()
        self.name = ls[0]
        self.surname = ls[1]
        self.salary = float(ls[2])
        self.duty = ls[3]
        self.norm = int(ls[4])
        self._hours = 0
        self.income = 0

    def _calc_income(self):
        if self.norm < self._hours:
            income = self.salary * (1 + (2 / self.norm) * (self.hours - self.norm))
        else:
            income = self.salary * (self.hours / self.norm)
        self.income = round(income, 2)

    @property
    def id(self):
        return f"{self.name} {self.surname}"

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, value):
        self._hours = value
        self._calc_income()


workers = {}
with open('data/workers', encoding='utf-8') as f:
    f.readline()
    for line in f:
        worker = Worker(line)
        workers.update({worker.id: worker})

with open('data/hours_of', encoding='utf-8') as f:
    f.readline()
    for line in f:
        ls = line.split()
        worker_id = f'{ls[0]} {ls[1]}'
        hours = int(ls[2])
        worker = workers.get(worker_id)
        if worker:
            worker.hours = int(ls[2])

for worker in workers.values():
        print(f'{worker.id} заработал {worker.income}')