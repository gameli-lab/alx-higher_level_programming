#!/usr/bin/python3
for i in range(100):
    for j in range(i + 1, 10):
        if (i != j):
            if (i * 10 + j == 89):
                print("{:02}".format(i * 10 + j), end='\n')
            else:
                print("{:02}".format(i * 10 + j), end=', ')
