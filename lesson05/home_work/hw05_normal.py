import os
import os.path
import hw05_easy

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


def change_current_directory():
    new_path = input('Введите название папки: ')
    if os.path.exists(new_path):
        try:
            os.chdir(new_path)
            print(f'Текущая директория изменена на {new_path}')
        except:
            print(f'Ошибка смены директории')
    else:
        print(f'Директория {new_path} отсутствует')


def show_list_dir():
    hw05_easy.show_path_content(False)


def remove_folder():
    del_dir = input('Введите название директории: ')
    hw05_easy.delete_directory(del_dir)


def create_new_folder():
    new_dir = input('Введите название директории: ')
    hw05_easy.create_directory(new_dir)


def show_menu():
    print('1. Перейти в папку')
    print('2. Просмотреть содержимое текущей папки')
    print('3. Удалить папку')
    print('4. Создать папку')
    print('0. Выход')


actions = {
    '1': change_current_directory,
    '2': show_list_dir,
    '3': remove_folder,
    '4': create_new_folder
}

print('Программа для работы с текущей папкой')
while True:
    show_menu()
    action = input('Выберите действие: ')
    if action == '0':
        break
    elif action in actions:
        actions[action]()
    else:
        print('Ввод не распознан повторите еще раз')
    print()
