#!/usr/bin/python3

"""
This module difines a rectangle
"""


class Rectangle:
    """ This class describes the rectangle """
    def __init__(self, width, height):
        """ Initializing a rectangle """
        self.__width = width
        self.__height = height


        def width(self):
            """ Getting the width """
            return (self.__width)

        def width(self, value):
            """ Setting the width """
            self.__width = value
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")

            def height(self):
                """ Getting height """
                return(self.__height)

            def height(self, value):
                """ Setting height"""
                self.__height = value
                if not isinstance(value, int):
                    raise TypeError("height must be an integer")
                if value < 0:
                    raise ValueError("height must be >= 0")
