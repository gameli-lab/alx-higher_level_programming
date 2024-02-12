#!/usr/bin/python3
from models.base import Base
'''This module defines a base class'''


class Rectangle(Base):
    '''This is the rectangle class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    #getter and setter methods for width
    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    #getter and setter methods for height
    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    #getter and setter methods for x
    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    #getter and setter methods for y
    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    #method for area of the rectangle
    def area(self):
        '''This method calculates the area of the rectangle'''
        return (self.__width * self.__height)

    #printing the rectangle with #
    def display(self):
        '''Prints the rectangle with  pound'''
        for i in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    #string representation of the rectangle
    def __str__(self):
        '''Preints the string rep of the rectangle'''
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, \
            self.__x, self.__y, self.__width, self.__height))

    #adding updater
    def update(self, *args, **kwargs):
        '''This method updates each attribute with both args and kwargs'''
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >=3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]

        for key, value in kwargs.items():
            if key == 'id':
                self.id = value
            elif key == 'width':
                self.__width = value
            elif key == 'height':
                self.__height = value
            elif key == 'x':
                self.__x = value
            elif key == 'y':
                self.__y = value

    def to_dictionary(self):
        '''This defines a dictionary rep of the rectangle'''
        return ({
            "id":self.id,
            "width":self.__width,
            "height":self.__height,
            "x":self.__x,
            "y":self.__y
            })
