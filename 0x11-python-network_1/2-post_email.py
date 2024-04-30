#!/usr/bin/python3
'''header module'''

import urllib.request, urllib.parse
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    email = urllib.parse.urlencode(email)
    email = email.encode('ascii')

    req = urllib.request.Request(url, email)
    with urllib.request.urlopen(req) as res:
        body = res.read().decode('UTF-8')

    print(body)
