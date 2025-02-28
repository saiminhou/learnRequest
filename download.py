import requests

url = 'https://www.example.com/api/download'
response = requests.get(url, stream=True)
f = open("example.txt", "wb")
# 循环去读取信息写入，chunk_size=512文件大小
for chunk in response.iter_content(chunk_size=512):
    if chunk:
        # 把循环读取的值，写入example.txt文件
        f.write(chunk)

with open('example.txt', 'wb') as f:
    f.write(response.content)