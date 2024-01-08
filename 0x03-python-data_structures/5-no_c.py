#!/usr/bin/python3
def no_c(my_string):
    new_string = ''.join(item for item in my_string if item.lower() not in ['c', 'C'])
    print("{}".format(new_string))
