#!/usr/bin/python3
"""This module inherits from list"""


class MyList(list):
    """This class has inherited list"""
    def print_sorted(self):
        """This function prints sorted list"""
        return (sorted(list(self)))
