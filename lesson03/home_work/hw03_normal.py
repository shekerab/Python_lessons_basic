# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
import turtle


def fibonacci(n, m):
    seq = [1, 1]
    for i in range(2, m):
        seq.append(seq[i - 1] + seq[i - 2])
    return seq[n - 1:m]


n, m = 5, 7
print(f'Последовательность {n}..{m}: {fibonacci(n, m)}')


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    sorted_list = origin_list[:]
    for i in range(len(sorted_list)):
        for j in range(i + 1, len(sorted_list)):
            if sorted_list[j] < sorted_list[i]:
                sorted_list[j], sorted_list[i] = sorted_list[i], sorted_list[j]
    return sorted_list


print('Отсортированный список:', sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(function, iterable):
# На вход принимается любой итерируемый объект
    for el in iterable:
        if function(el):
            yield el


my_list = [1, 2, 3, 4, 5, 6, 7]
filtered = list(my_filter(lambda x: x > 5, my_list))
print(f'Применяем фильтр: {my_list} -> {filtered}')

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def is_parallelogram(p1, p2, p3, p4):
    def k(a, b):
        return (b[1] - a[1]) / (b[0] - a[0])

    return k(p1, p2) == k(p3, p4) and k(p2, p3) == k(p4, p1)


def show_polygon(*args):
    turtle.up()
    turtle.goto(args[0])
    turtle.down()
    for p in args[1:]:
        turtle.goto(p)
    turtle.goto(args[0])
    turtle.mainloop()


a1, a2, a3, a4 = (0, 0), (50, 100), (200, 100), (150, 0)
print(f'Проверка на паралеллограмм {is_parallelogram(a1, a2, a3, a4)}')
show_polygon(a1, a2, a3, a4)
