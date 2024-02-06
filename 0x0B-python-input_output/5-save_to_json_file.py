#!/usr/bin/python3
"""This module saves to file"""
import json


def save_to_json_file(my_obj, filename):
    """This class saves to json file"""
    with open(filename, "w", "utf-8") as file:
        file.write(json.dumps(my_obj))
