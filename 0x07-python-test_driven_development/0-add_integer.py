#!/usr/bin/python3

""" This module defines an addition class """


def add_integer(a, b=98):
    """ This function defines an addition """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
