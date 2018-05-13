__author__ = 'Шекера Борис'

# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True

# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось?

# Подсказка: это значение точно есть ;)


class f:
    def __init__(self,num):
        self.num = num
    def __eq__(self, other):
        return True
    def __gt__(self, other):
        return True
    def __mul__(self, other):
        return self.num*other
    def __pow__(self, other):
        return self.num**other

a = f(1)
print(a == a**2, a == a*2, a > 999999)

a = float('inf')
print(a == a**2, a == a*2, a > 999999)
