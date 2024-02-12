#!/usr/bin/python3
'''This module defines a base class'''


class Base:
    '''This is the base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
