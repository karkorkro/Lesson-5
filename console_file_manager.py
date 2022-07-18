import os
import shutil
import platform
import bank_account
from quiz import victory
from quiz import pshkn

menu = 'создать папку;' \
       'удалить (файл/папку);' \
       'копировать (файл/папку);' \
       'просмотреть содержимое рабочей директории;' \
       'посмотреть только папки;' \
       'посмотреть только файлы;' \
       'просмотреть информацию об операционной системе;' \
       'посмотреть информацию о создателе программы;' \
       'играть в викторину;' \
       'войти в программу "банковский счет";' \
       'сменить рабочую директорию;' \
       'выйти'
menu = menu.split(';')
print(menu)
print(len(menu))
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
        current_dir = os.listdir(os.getcwd())
        dirs = []
        for file in current_dir:
            if os.path.isdir(file): dirs.append(file)
        print(dirs)
    elif action == 6:
        current_dir = os.listdir(os.getcwd())
        files = []
        for file in current_dir:
            if os.path.isfile(file): files.append(file)
        print(files)
    elif action == 7:
        print(platform.uname())
    elif action == 8:
        print('God is an only true creator of everything, we are just altering his creations')
    elif action == 9:
        victory(pshkn)
    elif action == 10:
        bank_account.accounting()
    elif action == 11:
        pathtofile = input('Введите путь')
        os.chdir(f'{pathtofile}')
    elif action == 12:
        break
    else:
        print('Неверный номер действия')
