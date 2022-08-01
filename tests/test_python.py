import pytest
import math


@pytest.mark.parametrize('f_concept, f_object, expected_result',
                         # отфильтровывает все, что не является цифрами
                         [(str.isdigit, ['one', 'two', 'list', '', 'dict', '100', '1', '50'], ['100', '1', '50']),
                          # оставляет четные числа
                          (lambda x: x % 2 == 0, [10, 111, 102, 213, 314, 515], [10, 102, 314]),
                          # оставляет слова, в которых больше 2х букв
                          (lambda x: len(x) > 2, ['one', 'no', 'list', '', 'dict'], ['one', 'list', 'dict'])])
def test_filter(f_concept, f_object, expected_result):
    assert list(filter(f_concept, f_object)) == expected_result


def test_filter_no_function():
    assert list(filter(None, ['bool', 0, None, True, False, 1, 1 - 1, 2 % 2])) == ['bool', True, 1]


def test_map():
    assert list(map(lambda x: x * 2 + 3, [10, 15, 21, 33, 42, 55])) == [23, 33, 45, 69, 87, 113]


def test_words_map():
    assert list(map(len, ["Welcome", "to", "Real", "Python"])) == [7, 2, 4, 6]


@pytest.mark.parametrize('it_object, expected_result',
                         [(['one', 'two', 'list', '', 'dict'], ['', 'dict', 'list', 'one', 'two']),
                          ('long string', [' ', 'g', 'g', 'i', 'l', 'n', 'n', 'o', 'r', 's', 't'])])
def test_sorted(it_object, expected_result):
    assert sorted(it_object) == expected_result


@pytest.mark.parametrize('it_object, sort_key, expected_result',
                         # сортирует по длине слова
                         [(['one', 'two', 'list', '', 'dict'], len, ['', 'one', 'two', 'list', 'dict']),
                          # сортирует сначала нечетные, потом четные
                          ([3, 6, 3, 2, 4, 8, 23], lambda x: x % 2 == 0, [3, 3, 23, 6, 2, 4, 8])])
def test_sorted_user_key(it_object, sort_key, expected_result):
    assert sorted(it_object, key=sort_key) == expected_result


def test_math_pi():
    assert math.pi == 3.141592653589793


@pytest.mark.parametrize('x, y, expected_result',
                         [(2, 3, 8), (3, 6, 729), (5, 4, 625)])
def test_math_pow(x, y, expected_result):
    assert math.pow(x, y) == expected_result


def test_math_sqrt():
    assert math.sqrt(16) == 4
    assert math.sqrt(25) == 5
    assert math.sqrt(81) == 9


def test_math_hypot():
    assert math.hypot(10, 40) == 41.23105625617661
