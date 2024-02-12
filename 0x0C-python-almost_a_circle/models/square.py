#!/usr/bin/python3
from models.rectangle import Rectangle
'''This module defines a square class'''


class Square(Rectangle):
    '''This is a square class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''This method initialiases the class'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns the string rep'''
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))

    # getter and seter methods for size
    @property
    def size(self):
        '''returns the value of size'''
        return (self.width)

    @size.setter
    def size(self, value):
        '''sets the value for size'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        for key, value in kwargs.items():
            if key == 'id':
                self.id = value
            elif key == 'size':
                self.width = value
            elif key == 'x':
                self.x = value
            elif key == 'y':
                self.y = value

    def to_dictionary(self):
        '''This returns the dictionary rep of the square'''
        return ({
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
            })
