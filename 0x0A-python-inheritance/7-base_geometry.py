#!/usr/bin/python3
'''this module defines a class base geometry'''


class BaseGeometry:
    '''this class is for base geometry'''
    def area(self):
        '''this message defines an area'''
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        '''this method validate integers'''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
