# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.


class Human:
    def __init__(self, name, second_name, surname):
        self.name = name
        self.surname = surname
        self.second_name = second_name

    def __str__(self):
        return f'{self.surname} {self.name[0]}. {self.second_name[0]+"." if self.second_name else ""}'

    @property
    def fullname(self):
        return f'{self.surname} {self.name}{" "+self.second_name if self.second_name else ""}'


class Subject:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Teacher(Human):
    def __init__(self, name, second_name, surname, class_rooms, subject):
        super().__init__(name, second_name, surname)
        self.name = name
        self.subject = subject
        self.class_rooms = class_rooms

    def __str__(self):
        return f'{self.fullname} ({self.subject.name})'


class ClassRoom:
    def __init__(self, number, char):
        self.char = char
        self.number = number

    @property
    def name(self):
        return f'{self.number}{self.char}'

    def __str__(self):
        return self.name


class Pupil(Human):
    def __init__(self, name, second_name, surname, class_room, mother, father):
        super().__init__(name, second_name, surname)
        self.class_room = class_room
        self.mother = mother
        self.father = father


subjects = [Subject('Math'), Subject('History'), Subject('Geography')]
class_rooms = [ClassRoom(5, 'a'), ClassRoom(5, 'b'), ClassRoom(6, 'a'), ClassRoom(6, 'b'), ClassRoom(6, 'c')]
teachers = [
    Teacher('Иван', 'Петрович', 'Сергеев', class_rooms[0:2], subjects[0]),
    Teacher('Юрий', 'Николаевич', 'Иващенко', class_rooms[2:3], subjects[0]),
    Teacher('Алексей', 'Казбекович', 'Сергеев', class_rooms[2:], subjects[1]),
    Teacher('Дмитрий', 'Олегович', 'Иванов', class_rooms[:2], subjects[2])
]

pupils = [
    Pupil('Станислав',
          'Яковлевич',
          'Ильин',
          class_rooms[0],
          Human('Елена', 'Петровна', 'Ильина'),
          Human('Яков', 'Сергеевич', 'Ильин')
          ),
    Pupil('Харитон',
          'Рудольфович',
          'Сазонов',
          class_rooms[0],
          Human('Елена', 'Николаевна', 'Сазонова'),
          Human('Рудольф', 'Рудольфович', 'Сазонов')
          ),
    Pupil('Ипполит',
          'Оскарович',
          'Егоров',
          class_rooms[0],
          Human('Елена', 'Петровна', 'Егорова'),
          Human('Оскар', 'Сергеевич', 'Егоров')
          ),
    Pupil('Иван',
          'Робертович',
          'Князев',
          class_rooms[1],
          Human('Елена', 'Петровна', 'Князева'),
          Human('Роберт', 'Иванович', 'Князев')
          )
]


# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
print('Список классов школы:')
print([str(c) for c in class_rooms])

# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
print('\nСписок учеников 5a класса:')
print([str(p) for p in pupils if p.class_room.name == '5a'])

# 3. Получить список всех предметов указанного ученика
# #  (Ученик --> Класс --> Учителя --> Предметы)
pupil = pupils[1]
print(f'\nСписок предметов ученика {pupil}:')
print([str(teacher.subject) for teacher in teachers if pupil.class_room in teacher.class_rooms])

# 4. Узнать ФИО родителей указанного ученика
pupil = pupils[2]
print(f'\nРодители ученика {pupil}:')
print(f'мама: {pupil.mother.fullname}, папа:{pupil.mother.fullname}')

# 5. Получить список всех Учителей, преподающих в указанном классе
class_room = class_rooms[1]
print(f'\nСписок учителей класса {class_room}:')
print([str(teacher) for teacher in teachers if class_room in teacher.class_rooms])
