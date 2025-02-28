import time
import requests

url = 'http://10.242.103.215:8080/'

print(time.strftime('%Y-%m-%d %H:%M:%S'))
try:
    html = requests.get(url, timeout=5).text
    print('success')
except requests.exceptions.RequestException as e:
    print(e)

print(time.strftime('%Y-%m-%d %H:%M:%S'))

import time
import requests

try:
    r = requests.get('https://github.com', timeout=(1, 2))
    print('success')
except requests.exceptions.RequestException as e:
    print(e)

print(time.strftime('%Y-%m-%d %H:%M:%S'))