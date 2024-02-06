#!/usr/bin/python3
""" This module writes to a file"""


def write_file(filename="", text=""):
    """ This function writes to a file"""
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)
