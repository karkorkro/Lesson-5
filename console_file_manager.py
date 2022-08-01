import os
import shutil
import platform
import bank_account
from quiz import victory
from quiz import pshkn


def files_list():
    files = [file for file in os.listdir() if os.path.isfile(file)]
    return files


def dirs_list():
    folders = [folder for folder in os.listdir() if os.path.isdir(folder)]
    return folders


menu = 'создать папку;' \
       'удалить (файл/папку);' \
       'копировать (файл/папку);' \
       'просмотреть содержимое рабочей директории;' \
       'посмотреть только папки;' \
       'посмотреть только файлы;' \
       'записать информацию о файлах и папках в файл;' \
       'просмотреть информацию об операционной системе;' \
       'посмотреть информацию о создателе программы;' \
       'играть в викторину;' \
       'войти в программу "банковский счет";' \
       'сменить рабочую директорию;' \
       'выйти'
menu = menu.split(';')

if __name__ == '__main__':
    while True:
        for i in menu:
            print(f' Чтобы {i}, нажмите {menu.index(i) + 1}')
        action = int(input('Введите действие: '))
        if action == 1:
            name = input('Введите название папки')
            if not os.path.exists(f'{name}'):
                os.mkdir(f'{name}')
        elif action == 2:
            name = input('Введите название файла')
            if os.path.exists(f'{name}'):
                path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'{name}')
                os.remove(path)
            else:
                print('Файл не найден')
        elif action == 3:
            name = input('Введите название файла: ')
            new_name = input('Введите название для копии: ')
            shutil.copy(f'{name}', f'{new_name}')
        elif action == 4:
            print(os.listdir(os.getcwd()))
        elif action == 5:
            print(dirs_list())
        elif action == 6:
            print(files_list())
        elif action == 7:
            with open('listdir.txt', 'w') as f:
                f.write('Folders: ' + ','.join(dirs_list()) + '\n')
                f.write('Files: ' + ','.join(files_list()))
        elif action == 8:
            print(platform.uname())
        elif action == 9:
            print('God is an only true creator of everything, we are just altering his creations')
        elif action == 10:
            victory(pshkn)
        elif action == 11:
            bank_account.accounting()
        elif action == 12:
            path_to_file = input('Введите путь')
            os.chdir(f'{path_to_file}')
        elif action == 13:
            break
        else:
            print('Неверный номер действия')
