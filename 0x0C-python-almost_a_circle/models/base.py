#!/usr/bin/python3

'''
This module defines a base class
'''
import json


class Base:
    '''
    This is the definition of the base class
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        returns the JSON string representation
        '''
        if list_dictionaries is None:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        writes the JSON string representation
        '''
        if list_objs is None:
            return ([])

        gameli = cls.__name__ + ".json"
        with open(gameli, "w") as file:
            json_str = cls.to_json_string([obj.to_dictionary()
                                          for obj in list_objs])
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        '''
        returns the list of the JSON string representation
        '''
        if json_string is None:
            json_string = []

        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        '''
        returns an instance with all attributes already set

        Args:
        dictionary
                a double pointer to a dictionary
        '''
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)

        elif cls.__name__ == "Square":
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)
        return (dummy_instance)

    @classmethod
    def load_from_file(cls):
        '''
        returns a list of instances
        '''
        gameli = cls.__name__ + ".json"

        try:
            with open(gameli, "r") as torfu:
                json_str = torfu.read()
                dicts = cls.from_json_string(json_str)
                return ([cls.create(**dictionary) for dictionary in dicts])
        except FileNotFoundError:
            return ([])

    @staticmethod
    def to_csv_string(inst):
        '''
        Convert an instance to CSV format.
        '''

        if isinstance(inst, Rectangle):
            return "{},{},{},{},{}".format(inst.id, inst.width, inst.height,
                                           inst.x, inst.y)
        elif isinstance(inst, Square):
            return "{},{},{},{}".format(inst.id, inst.size, inst.x, inst.y)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''
        Serialises instances from CSV format
        '''
        if list_objs is None:
            return ([])

        gameli = cls.__name__ + ".csv"
        with open(gameli, "w") as torfu:
            for obj in list_objs:
                csv_line = cls.to_csv_string(obj)
                torfu.write(csv_line + '\n')

    @classmethod
    def load_from_file_csv(cls):
        '''
       Deserialize instances from CSV format and return a list of instances.
        '''

        gameli = cls.__name__ + ".csv"
        try:
            with open(gameli, "r") as torfu:
                instances = []
                for line in torfu:
                    data = line.strip().split(',')
                    if cls.__name__ == "Rectangle":
                        instance = cls(int(data[1]), int(data[2]),
                                       int(data[3]), int(data[4]),
                                       int(data[0]))
                    elif cls.__name__ == "Square":
                        instance = cls(int(data[1]), int(data[2]),
                                       int(data[3]), int(data[0]))
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []
