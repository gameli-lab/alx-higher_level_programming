#!/usr/bin/python3

"""
This module difines a rectangle
"""


class Rectangle:
    """ This class describes the rectangle """
    def __init__(self, width=0, height=0):
        """ Initializing a rectangle """
        self.__width = width
        self.__height = height

        @property
        def width(self):
            """ Getting the width """
            return (self.__width)

        @width.setter
        def width(self, value):
            """ Setting the width """
            self.__width = value
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

            @property
            def height(self):
                """ Getting height """
                return (self.__height)

            @height.setter
            def height(self, value):
                """ Setting height"""
                self.__height = value
                if not isinstance(value, int):
                    raise TypeError("height must be an integer")
                if value < 0:
                    raise ValueError("height must be >= 0")
                self.__height = value

            @property
            def area(self):
                """defines an area of a rectangle """
                return (width * height)

            @property
            def perimeter(self):
                """ defines the perimeter of a rectangle """
                return ((2 * width) + (2 * height))
