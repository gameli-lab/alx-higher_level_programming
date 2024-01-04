#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if ('a' <= str <= 'z'):
            result += chr(ord(char)) - ord('a') + ord('A')
        else:
            result += char

    return (result)
