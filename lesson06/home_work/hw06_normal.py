# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
# #  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Human:
    def __init__(self, name, surname, second_name):
        self.name = name
        self.surname = surname
        self.second_name = second_name

    def __str__(self):
        return f'{self.surname} {self.name[0]}. {self.second_name[0]+"." if self.second_name else ""}'


class Subject:
    def __init__(self, name):
        self.name = name


class Teacher(Human):
    def __init__(self, name, surname, second_name, subject, class_rooms):
        super().__init__(name, surname, second_name)
        self.name = name
        self.subject = subject
        self.class_rooms = class_rooms


class ClassRoom:
    def __init__(self, name, teachers):
        self.name = name
        self.teachers = teachers


class Pupil(Human):
    def __init__(self, name, surname, second_name, class_room, mother, father):
        super().__init__(name, surname, second_name)
        self.class_room = class_room
        self.mother = mother
        self.father = father


subjects = [Subject('Math'), Subject('History'), Subject('Geography')]




# class School:
#     def __init__(self, class_rooms, teachers):
#         self.class_rooms = class_rooms
#         self.teachers = teachers