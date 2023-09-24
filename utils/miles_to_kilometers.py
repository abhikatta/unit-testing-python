'''
Simple module that works with distance conversions
'''


def to_kilometers(miles: int or float) -> int or float:
    '''
    Convert miles to kilometers.
    '''
    return miles*1.60934


def to_miles(kilometers: int or float) -> int or float:
    '''
    Convert kilometers to miles.
    '''
    return kilometers/1.60934
