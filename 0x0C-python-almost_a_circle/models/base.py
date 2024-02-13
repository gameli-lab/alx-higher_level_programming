#!/usr/bin/python3

'''This module defines a base class'''

import json


class Base:
    '''This is the base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    def to_json_string(list_dictionaries):
        '''returns the JSON string representation'''
        if list_dictionaries is None:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))
