# import requests
#
# url = "https://httpbin.org/post"
# # 设置请求头
# headers = {'Content-Type': 'text/xml'}
# # 比如上传本地文件file.py,使用files参数
# r = requests.post(url=url, files={'file': open('day1.py', 'rb')}, headers={'Content-Type': 'binary'})
# print(r.text)
#
# # 需提前安装requests_toolbelt库， pip install requests_toolbelt
# from requests_toolbelt import MultipartEncoder
# # 导入 requests包
# import requests
#
# # 需要上传文件,如本地的file.py文件
# m = MultipartEncoder(
#     fields={'field0': 'value', 'field1': 'value',
#             'field2': ('filename', open('day1.py', 'rb'), 'text/plain')}
# )
#
# r_file = requests.post('http://httpbin.org/post', data=m,
#                        headers={'Content-Type': m.content_type})
# print(r_file.text)
# # 不需要文件
# m = MultipartEncoder(fields={'field0': 'value', 'field1': 'value'})
#
# r = requests.post('http://httpbin.org/post', data=m,
#                   headers={'Content-Type': m.content_type})
# print(r.text)

import json
import requests

url = "https://httpbin.org/post"
# 设置请求头
headers = {'Content-Type': 'text/xml'}
# 传入xml格式文本
r_xml = requests.post(url=url, data='<?xml  ?>', headers=headers)
print(r_xml.text)

# 传入json格式文本,有两种方法，1、使用data，2、使用json参数
# 使用data参数
r_data = requests.post(url=url, data=json.dumps({'key1': 'value1', 'key2': 'value2'}),
                       headers={'Content-Type': 'application/json'})
print(r_data.text)
# 使用json参数
r_json = requests.post(url=url, json=json.dumps({'key1': 'value1', 'key2': 'value2'}),
                       headers={'Content-Type': 'application/json'})
print(r_json.text)

import requests

url = "https://httpbin.org/post"
# 设置请求头
headers = {'Content-Type': 'text/xml'}
# 比如上传本地文件file.py,使用files参数
r = requests.post(url=url, files={'file': open('README.md', 'rb')}, headers={'Content-Type': 'binary'})
print(r.text)