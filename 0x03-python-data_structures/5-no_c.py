#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    for item in my_string:
        if item.lower() not in ['c', 'C']:
            new_string += item

    return (new_string)
