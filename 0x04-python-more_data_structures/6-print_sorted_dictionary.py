#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary)

    for key in sorted_dict:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
