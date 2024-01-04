#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5

    p = a + b
    q = a - b
    r = a * b
    s = a / b

    print("{} + {} = {}".format(a, b, p))
    print("{} - {} = {}".format(a, b, q))
    print("{} * {} = {}".format(a, b, r))
    print("{} / {} = {}".format(a, b, s))
