#!/usr/bin/python3
'''header module'''
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as res:
        req_id = res.headers.get('X-Request-Id')
        print('{}'.format(req_id))
