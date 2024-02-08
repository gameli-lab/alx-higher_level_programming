#!/usr/bin/python3
'''this module find inheritance'''


def inherits_from(obj, a_class):
    '''this method function inheritance from any class'''
    return (any(issubclass(type(obj), a_class) /
            for a_class in cls.__subclasses__()) /
            or any(is_subclass_instance(obj, a_class) /
            for a_class in cls.__subclasses__()))
