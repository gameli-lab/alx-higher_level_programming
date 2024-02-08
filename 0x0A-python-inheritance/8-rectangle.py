#!/usr/bin/python3
'''this module define rectangle that inherits from base geometry'''


class Rectangle(BaseGeometry):
    '''this class inherit from base geometry'''
    def __init__(self, width, height):
        '''this method initializes the class'''
        super().__init__
        self.width = width
        self.height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
