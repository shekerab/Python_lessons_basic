import random

AUTOMATIC_MODE = True # если True не нужно вводить y, n на каждом шаге


class LotoCard:
    LINES = 3 # константы класса, можно переопределить еще не создав ни одного объекта
    COLUMNS = 9
    FILLED_COLUMNS = 5
    MAX_NUMBER = 90

    def __init__(self, title):
        self.lines = []
        self.title = title
        self._generate_values()

    def _generate_values(self):
        bank = list(range(1, self.MAX_NUMBER+1)) # набор чисел 1..90
        for i in range(self.LINES):
            line = random.sample(bank, self.FILLED_COLUMNS) # выборка пяти случайных уникальных элементов
            line.sort() # сортируем по возрастанию
            for x in line: # убираем из банка выбранные значения
                bank.remove(x)
            for x in range(self.COLUMNS - self.FILLED_COLUMNS): # заполняем недостающие пустыми
                index = random.randint(0, len(line)) # берем случай индекс от 0 до последний индекс + 1
                line.insert(index, None) # вставляем пустое значение
            self.lines.append(line)

    def check_number(self, number):
        for line in self.lines:
            if number in line:
                index = line.index(number)
                if index > -1:
                    line[index] = ' ++'
                    return True
        return False

    @property
    def is_finished(self):
        for line in self.lines:
            for column in line:
                if column and type(column) == int:
                    return False
        return True # не найдено ни одного числа

    def print(self):
        decor_len = (4 * self.COLUMNS - len(self.title)) // 2
        print('-' * decor_len, self.title, '-' * decor_len)
        for line in self.lines:
            line_str = f'|'
            for column in line:
                if column:
                    line_str += f'{column:>3}|'
                else:
                    line_str += '   |'
            print(line_str)
        print('-' * (4 * self.COLUMNS + 1))


# основной цикл
def get_user_answer(question, variants):
    while True: # допускаем ошибку пользоватея при вводе
        answer = input(f'{question} ({variants[0]} / {variants[1]}):').lower()
        if answer not in variants:
            print('Введите корректный ответ')
            continue
        return answer


def num_generator():
    bank_numbers = list(range(1, LotoCard.MAX_NUMBER + 1))  # числа от 1 до 90
    while len(bank_numbers) > 0:
        number = random.choice(bank_numbers) # выбираем случайный номер из имеющихся
        bank_numbers.remove(number)  # выбранный удаляем
        yield number
    else:
        raise StopIteration


player_card = LotoCard('Ваша карточка')
computer_card = LotoCard('Карточка компьютера')


for number in num_generator():
    player_card.print()
    computer_card.print()
    print(f'Выпал номер {number}')
    computer_card.check_number(number)
    player_number_result = player_card.check_number(number)

    if AUTOMATIC_MODE: # можно отключить издевательское условие на внимательность вводить y, n
        answer = input('Нажмите любую клавишу для продолжения')
    else:
        answer = get_user_answer('Зачеркнуть цифру?', ('y', 'n'))
        if answer == 'y':
            if not player_number_result:
                print(f'Номера {number} на карточке нет, Вы проиграли')
                break
        else:
            if player_number_result:
                print(f'Номер {number} на карточке есть, Вы проиграли')
                break

    if player_card.is_finished:
        if computer_card.is_finished:
            print('Игра закончена, ничья')
            break
        else:
            print('Ваша карточка полностью закрыта, Вы выиграли!')
            player_card.print()
            computer_card.print()
            break
    elif computer_card.is_finished:
        print('Карточка компьютера полностью закрыта, Вы проиграли!')
        computer_card.print()
        player_card.print()
        break

    print()# отступ

