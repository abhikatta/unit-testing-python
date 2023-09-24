'''
Simple module that works with distance conversions
'''
import pytest


class DistanceConversion:
    """Class for converting distance meterics from one to another.
    """

    def __init__(self) -> None:
        pass

    @staticmethod
    def to_kilometers(miles: int or float) -> int or float:
        '''
        Convert miles to kilometer.
        '''
        try:
            miles = float(miles)
            return miles*1.60934
        except ValueError:
            raise ValueError("Input should only be an integer or float.")

    @staticmethod
    def to_miles(kilometers: int or float) -> int or float:
        '''
        Convert kilometers to miles.
        '''
        try:
            kilometers = float(kilometers)
            return kilometers/1.60934
        except ValueError:
            raise ValueError("Input should only be an integer or float.")
