#!/usr/bin/python3
'''This is a urlopen module'''
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
    body = res.read()
    dec = body.decode('UTF-8')

    print('Body response:')
    print('\t - type: {}'.format(type(body)))
    print('\t - content: {}'.format(body))
    print('\t - utf8 content: {}'.format(dec))
