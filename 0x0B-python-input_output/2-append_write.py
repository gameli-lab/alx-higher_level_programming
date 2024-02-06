#!/usr/bin/python3
"""This module appends"""


def append_write(filename="", text=""):
    """This function appends data to a file"""
    with open(filename, mode='a', encoding='utf-8' as file:
              file.append(text)
