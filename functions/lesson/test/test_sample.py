from lesson import add_one, division, sum_, p, count_factorial
import pytest

def test_answer():
    assert add_one(3) == 4
    assert add_one(9) == 10


def test_division():
    assert division(9, 3) == 3

def test_division2():
    with pytest.raises(ZeroDivisionError):
        division(9, 0)

    

def test_sum_():
    t = [[1, 2, 3], [3, 4, 7], [8, 5, 13]]
    for i in t:
        assert sum_(i[0], i[1]) == i[2]



def test_p():
    test_case = [('Dad', True), ('Привет', False)]
    for case in test_case:
        assert p(case[0]) == case[1]
    # assert p('Mom') == True


def test_count_f():
    from math import factorial
    assert count_factorial(10) == factorial(10)