# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import hw05_easy


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp <file_name> - создание копии указанного файла")
    print("rm <file_name> - удаление указанного файла")
    print("cd <full_path or relative_path> - замена текущей директории на указанную")
    print("ls - отображение полного пути текущей директории")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def cp_file():
    hw05_easy.duplicate_file(dir_name)


def rm_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    answer = input(f'Точно удалить {dir_name}? y/n')
    if answer != 'y':
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.remove(dir_path)
        print('Файл {} удален'.format(dir_name))
    except FileNotFoundError:
        print('Файл {} не найден'.format(dir_name))


def cd_path():
    if not dir_name:
        print("Необходимо указать имя директори вторым параметром")
        return
    try:
        os.chdir(dir_name)
        print(f'Текущая директория сменена на {dir_name}')
    except:
        print("Ошибка смены директории на {dir_name}")


def ls_path():
    print(os.getcwd())


def ping():
    print("pong")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp_file,
    "rm": rm_file,
    "cd": cd_path,
    "ls": ls_path
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
