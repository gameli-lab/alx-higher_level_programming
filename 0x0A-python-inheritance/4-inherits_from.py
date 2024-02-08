#!/usr/bin/python3
'''this module find inheritance'''


def inherits_from(obj, a_class):
    '''this method function inheritance from any class'''
    return (any(issubclass(type(obj), subclass) /
            for subclass in cls.__subclasses__()) /
            or any(is_subclass_instance(obj, subclass) /
            for subclass in cls.__subclasses__()))
