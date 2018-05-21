# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math
import turtle


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Polygon:

    def __init__(self, *args):
        self.points = [None] # точки, 0 точку определим как None для читаемости
        for point in args:
             self.points.append(point)
        self.lines = [] # длины отрезков

    def show(self):
        turtle.up()
        turtle.goto(self.points[1].x, self.points[1].y)
        turtle.down()
        for p in self.points[2:]:
            turtle.goto(p.x, p.y)
        turtle.goto(self.points[1].x, self.points[1].y)
        turtle.mainloop()

    def _height(self, point, line_point_1, line_point_2):
        a = line_point_2.y - line_point_1.y
        b = line_point_2.x - line_point_1.x
        c = line_point_1.y * line_point_2.x - line_point_1.x * line_point_2.y
        h = abs(a * point.x + b * point.y + c) / (math.sqrt(a**2 + b**2))
        return h



class Triangle(Polygon):

    def square(self):
        return 0.5 * abs(
            (self.points[1].x - self.points[3].x) * (self.points[2].y - self.points[3].y) -
            (self.points[2].x - self.points[3].x) * (self.points[1].y - self.points[3].y)
        )

    def perimeter(self):
        line12_len = math.sqrt((self.points[1].x - self.points[2].x)**2 + (self.points[1].y - self.points[2].y)**2)
        line23_len = math.sqrt((self.points[2].x - self.points[3].x)**2 + (self.points[2].y - self.points[3].y)**2)
        line31_len = math.sqrt((self.points[3].x - self.points[1].x)**2 + (self.points[3].y - self.points[1].y)**2)
        return line12_len + line23_len + line31_len

    def heights(self):
        result = {
          1: self._height(self.points[1], self.points[2], self.points[3]),
          2: self._height(self.points[2], self.points[1], self.points[3]),
          3: self._height(self.points[3], self.points[1], self.points[2])
        }
        return result


triangle = Triangle(Point(0, 0), Point(100, 0), Point(0, 100))
triangle.show()
print(f'Площадь {triangle.square()}')
print(f'Периметр {triangle.perimeter()}')
print(f'Высоты из всез вершин {triangle.heights()}')


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trap(Polygon):

    def is_r(self):
        return (self.points[2].x - self.points[1].x) == (self.points[4].x - self.points[3].x) and \
               (self.points[2].x - self.points[1].x) == (self.points[4].x - self.points[3].x)
