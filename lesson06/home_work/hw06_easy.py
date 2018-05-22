# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import sqrt
import turtle


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:

    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2
        self.len = sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2) # длина отрезка
        self.a = point2.y - point1.y # a,b,c - коэфициенты уравнения ax+by+c=0 задающего прямую
        self.b = point2.x - point1.x # содержащую наш отрезок
        self.c = point1.y * point2.x - point1.x * point2.y

    def distance_from_point(self, point):
        return abs(self.a * point.x + self.b * point.y + self.c) / (sqrt(self.a**2 + self.b**2))

    def is_parallel(self, other):
        if self.b == 0 or other.b == 0: # если хоть одна прямая вертикальная
            return self.b == 0 and other.b # то паралельны, если обе вертикальны
        else:
            return self.a / self.b == other.a / other.b # равны уговые коэфициенты


class Polygon:

    def __init__(self, *args):
        self.points = [] # точки, класс Point
        for point in args:
             self.points.append(point)
        self.points.append(args[0])  # последняя точка - снова первая, потому что фигура замкнутая
        self.lines = [] # отрезки между вершинами class Line
        for i in range(len(self.points)-1):
            self.lines.append(Line(self.points[i], self.points[i+1]))

    def perimeter(self):
        return sum([line.len for line in self.lines]) # сумма длин всех отрезков

    def show(self):
        ttl = turtle.Turtle()
        ttl.up()
        ttl.goto(self.points[0].x, self.points[0].y)
        ttl.down()
        for p in self.points[1:]:
            ttl.goto(p.x, p.y)
        ttl.goto(self.points[0].x, self.points[0].y)


class Triangle(Polygon):

    def heights(self): # высота - расстояние от вершины до противополжной грани
        return [self.lines[1].distance_from_point(self.points[0]),
                self.lines[2].distance_from_point(self.points[1]),
                self.lines[0].distance_from_point(self.points[2])]

    def square(self): # школьная формула - площадь = 1/2 высоты на основание
        return 0.5 * self.heights()[0] * self.lines[1].len

    # периметр универсален, и определен в родительском классе как сумма отрезков


triangle = Triangle(Point(0, 0), Point(100, 0), Point(0, 100))
triangle.show()
print('Треугольник:')
print(f'Площадь {triangle.square()}')
print(f'Периметр {triangle.perimeter()}')
print(f'Высоты из всез вершин {triangle.heights()}\n')


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezium(Polygon):

    def is_valid(self): # трапеция?
        # верняя грань паралельна нижней
        # верняя грань не равна нижней
        return self.lines[1].is_parallel(self.lines[3]) and self.lines[1].len != self.lines[3].len

    def is_equilateral(self): # равнобокая ли?
        return self.lines[0].len == self.lines[2].len

    def height(self): # высота - расстояние от одной из верхних вершин до нижнего основания
        return self.lines[3].distance_from_point(self.points[1])

    def square(self): # школьная формула - площадь = высота * 1/2 (сумма оснований)
        return self.height() * 0.5 * (self.lines[1].len + self.lines[3].len)


trap = Trapezium(Point(-300, 0), Point(-250, 100), Point(-100, 100), Point(-50, 0))
trap.show()
turtle.mainloop()
print('Трапеция: ')
print(f'{"Трапеция задана верно" if trap.is_valid() else "Трапеция задана НЕ верно"}')
print(f'Трапеция {"равнобочная" if trap.is_equilateral() else "не равнобочная"}')
if trap.is_valid():
    print(f'Площадь {trap.square()}')
    print(f'Периметр {trap.perimeter()}')
    print(f'Высота {trap.height()}')

