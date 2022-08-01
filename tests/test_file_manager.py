import os
from quiz import check_answer
from console_file_manager import files_list
from console_file_manager import dirs_list


# тест единственной чистой функции из викторины
def test_check_answer():
    assert check_answer('a', 'a') is True
    assert check_answer('a', 'b') is False


# проверка грязных функций показывающих содержимое текущей директории

def test_files_list():
    assert files_list() == ['test_bank_account.py', 'test_file_manager.py', 'test_python.py']


def test_dirs_list():
    assert (dirs_list()) == ['.pytest_cache']


# тест грязной функции удаления файла, удаляет файл если он есть, если нет - создает и удаляет


def test_os_remove():
    if not os.path.exists('other.py'):
        open('other.py', 'w')
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'other.py')
    os.remove(path)
    assert not os.path.exists('other.py')
