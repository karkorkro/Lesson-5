from quiz import check_answer

#тест единственной чистой функции из викторины
def test_check_answer():
    assert check_answer('a', 'a') == True
    assert check_answer('a', 'b') == False

# тест грязной функции удаления файла, удаляет файл если он есть, если нет - создает и удаляет
import os
def test_os_remove():
    if os.path.exists('other.py'):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'other.py')
        os.remove(path)
    else:
        open('other.py', 'w')
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'other.py')
        os.remove(path)
    assert not os.path.exists('other.py')