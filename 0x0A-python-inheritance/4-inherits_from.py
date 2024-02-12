#!/usr/bin/python3
"""this is the documentation for this module. it's defines a functionthat finds inheritance of any form"""


def inherits_from(obj, a_class):
    '''this method function inheritance from any class'''
    return (any(issubclass(type(obj), a_class) /
            for a_class in cls.__subclasses__()) /
            or any(is_subclass_instance(obj, a_class) /
            for a_class in cls.__subclasses__()))
