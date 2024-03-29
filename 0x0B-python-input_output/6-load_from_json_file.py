#!/usr/bin/python3
"""This module creates an Object from a json file"""
import json


def load_from_json_file(filename):
    """This function creates obj from json"""
    with open(filename) as file:
        return (json.load(file))
