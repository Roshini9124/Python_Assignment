from src.NoIdea.util import calculate_happiness

def test_case_1():
    values = ['1', '5', '3']
    a = {'3', '1'}
    b = {'5', '7'}
    assert calculate_happiness(values, a, b) == 1


def test_case_2():
    values = ['1', '2', '3']
    a = {'1', '2'}
    b = {'3'}
    assert calculate_happiness(values, a, b) == 1


def test_case_3():
    values = ['1', '2', '3', '4']
    a = {'1', '3'}
    b = {'2', '4'}
    assert calculate_happiness(values, a, b) == 0


def test_case_4():
    values = ['5', '6']
    a = {'1', '2'}
    b = {'3', '4'}
    assert calculate_happiness(values, a, b) == 0


def test_case_5():
    values = ['1', '1', '2', '2']
    a = {'1'}
    b = {'2'}
    assert calculate_happiness(values, a, b) == 0
