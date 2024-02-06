#!/usr/bin/python3
"""This module saves to file"""
import json


def save_to_json_file(my_obj, filename):
    """This class saves to json file"""
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dumps(my_obj, file)
