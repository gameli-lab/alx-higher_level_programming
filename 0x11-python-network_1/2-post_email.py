#!/usr/bin/python3
'''header module
import urllib.request
import sys

url = sys.argv[1]
email = sys.argv[2]
coded = email.encode('UTF-8')

req = urllib.request.Request(url, data=coded, method='POST')
with urllib.request.urlopen(req) as res:
    body = res.read().decode('UTF-8')

    print(body)'''

import urllib.request
import sys

url = sys.argv[1]
email = sys.argv[2]

data = email.encode('utf-8')

req = urllib.request.Request(url, data=data, method='POST')

with urllib.request.urlopen(req) as response:
    body = response.read().decode('utf-8')
    print(body)
