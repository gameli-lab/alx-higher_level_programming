#!/usr/bin/python3
"""This module saves to file"""
import json


def save_to_json_file(my_obj, filename):
    """This class saves to json file"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
