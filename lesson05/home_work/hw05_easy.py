import os
import os.path
import sys
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def create_directory(dir_name):
    if os.path.exists(dir_name):
        print(f'Директория {dir_name} уже существует')
    else:
        try:
            os.mkdir(dir_name)
        except:
            print(f'Ошибка создания директории: {dir_name}')
        else:
            print(f'Директория {dir_name} создана')


if __name__ == '__main__':
    print('Задача 1:')
    script_dir = os.path.split(sys.argv[0])[0]
    print(script_dir)
    for i in range(1,10):
        create_directory(os.path.join(script_dir, f'dir_{i}'))


def delete_directory(dir_name):
    if os.path.exists(dir_name):
        try:
            os.removedirs(dir_name)
            print(f'dir_name {dir_name} удалена')
        except:
            print(f'Ошибка удаления директории')
    else:
        print(f'Директория {dir_name} отсутствует')


if __name__ == '__main__':
    for i in range(1,10):
        os.removedirs(os.path.join(script_dir, f'dir_{i}'))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# def show_folders2():
#     return next(os.walk('.'))[1]

def show_path_content(path, only_directories = False):
    print([x for x in os.listdir(path) if not only_directories or os.path.isdir(x)])


if __name__ == '__main__':
    show_path_content(os.getcwd(), True)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def duplicate_file(file_path):
    try:
        file_name, file_ext = os.path.splitext(file_path)
    except FileNotFoundError:
        print(f'Файл {file_full_path} не найден')
    new_file = f'{file_name}_copy{file_ext}'
    try:
        shutil.copy(file_path, new_file)
    except:
        print(f'Ошибка при копировании файла {file_path}')
    else:
        print(f'Файл {file_path} скопирован {new_file}')


if __name__ == '__main__':
    duplicate_file(sys.argv[0])
