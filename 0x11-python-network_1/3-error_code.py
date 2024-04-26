#!/usr/bin/python3
'''header module'''
import urllib.request
import sys

def main(argv):
    '''managing http error code'''
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as res:
            body = res.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))

if __name__ == '__main__':
    main(argv)
