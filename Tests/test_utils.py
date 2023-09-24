from utils.miles_to_kilometers import to_kilometers
from math import ceil


def test1():
    '''
    Simple first test
    '''
    assert ceil(to_kilometers(100)) == 161


def test2():
    assert to_kilometers(1) == 1.60934


def test3():
    assert to_kilometers(2) == 1.60934*2


def test4():
    assert to_kilometers(10) == 16.0934


def test5():
    assert to_kilometers(10*10) == (1.60934)*100
