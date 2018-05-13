import math


class Fraction:

    def __init__(self, str_fraction):
        if not str_fraction:
            return
        self.str_ = str_fraction.strip()
        splitted_by_space = self.str_.split(' ')
        if len(splitted_by_space) == 1:
            int_part = 0
            splitted_by_slash = splitted_by_space[0].split('/')
            if len(splitted_by_slash) == 1:
                int_part = int(splitted_by_slash[0])
                numerator = 0
                denominator = 1
                sign = -1 if int_part < 0 else 1
            else:
                numerator = int(splitted_by_slash[0])
                denominator = int(splitted_by_slash[1])
                sign = -1 if numerator < 0 else 1
        else:
            int_part = int(splitted_by_space[0])
            splitted_by_slash = splitted_by_space[1].split('/')
            numerator = int(splitted_by_slash[0])
            denominator = int(splitted_by_slash[1])
            sign = -1 if int_part < 0 else 1

        self.sign = sign
        self.numerator = abs(int_part) * denominator + abs(numerator)
        self.denominator = denominator
        self.beautify()

    def int_repr(self):
        # Представление в виде целая часть и числитель, знаменатель
        int_part = self.sign * (self.numerator // self.denominator)
        if int_part == 0:
            numerator = self.sign * (self.numerator % self.denominator)
        else:
            numerator = self.numerator % self.denominator
        denominator = self.denominator
        return int_part, numerator, denominator

    def init_by_simple_repr(self, numerator, denominator):
        # Инициализация объекта из представления в виде числитель, знаменатель
        self.sign = -1 if numerator < 0 else 1
        self.denominator = denominator
        self.numerator = abs(numerator)
        self.beautify()

    def beautify(self):
        # Сокращаем дробь
        while True:
            k = math.gcd(self.numerator, self.denominator)
            if k == 1:
                break
            self.numerator = self.numerator // k
            self.denominator = self.denominator // k

    def __str__(self):
        int_part, numerator, denominator = self.int_repr()
        if numerator == 0:
            return f'{int_part}'
        elif int_part == 0:
            return f'{numerator}/{denominator}'
        else:
            return f'{int_part} {numerator}/{denominator}'

    # def __repr__(self):
    #     int_part, numerator, denominator = self.int_repr()
    #     return f'Fraction("{int_part} {numerator}/{denominator}")'

    def __add__(self, other):
        numerator = self.sign * self.numerator * other.denominator + other.sign * other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        result = Fraction('')
        result.init_by_simple_repr(numerator, denominator)
        return result

    def __sub__(self, other):
        numerator = self.sign * self.numerator * other.denominator - other.sign * other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        result = Fraction('')
        result.init_by_simple_repr(numerator, denominator)
        return result