#!/usr/bin/python3
"""This module creates an Object from a json file"""


def load_from_json_file(filename):
    """This function creates obj from json"""
    with open(filename, encoding="utf-8") as file:
       return (json.load(file))
