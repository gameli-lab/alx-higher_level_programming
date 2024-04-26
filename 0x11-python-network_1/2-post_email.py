#!/usr/bin/python3
'''header module'''
import urllib.request
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    coded = email.encode('UTF-8')

    req = urllib.request.Request(url, data=coded, method='POST')
    with urllib.request.urlopen(req) as res:
        body = res.read().decode('UTF-8')

    print(body)
