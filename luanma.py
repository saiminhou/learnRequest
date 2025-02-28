import requests
import chardet

res = requests.get("https://www.baidu.com/")
res.encoding = res.apparent_encoding

try:
    txt = res.content.decode('gbk')
except UnicodeDecodeError as e:
    txt = res.content.decode('utf-8')

encoding = chardet.detect(res.content)['encoding']
# res.content.decode(encoding)
