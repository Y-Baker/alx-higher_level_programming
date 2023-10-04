#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status by urllib"""

from urllib.request import urlopen

if __name__ == '__main__':
    with urlopen('https://alx-intranet.hbtn.io/status') as res:
        output = res.read()
        print('Body response:')
        print('\t- type: ', type(output))
        print('\t- content: ', output)
        print('\t- utf8 content: ', output.decode('utf-8'))
