#!/usr/bin/python3
'''header module'''
import urllib.request
import sys

url = sys.argv[1]
try:
    with urllib.request.urlopen(url) as res:
        body = res.read().decode('utf-8')
        print(body)
except urllib.error.HTTPError as e:
    print('Error code: {}'.format(e.code))
