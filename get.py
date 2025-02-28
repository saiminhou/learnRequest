# 导入 requests包
import requests
# 设置请求参数
kw = {'s': 'python 教程'}
# 设置请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# 设置cookies
cookies = {"from-my": "browser"}
# 设置是否重定向
allow_redirects = False
# 设置超时时间
timeout = 5
# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
response = requests.get("https://www.runoob.com/", params=kw, headers=headers, cookies=cookies,allow_redirects=allow_redirects, timeout=timeout)
# 查看响应状态码
print(response.status_code)
# 查看响应头部字符编码
print(response.encoding)
# 查看完整url地址
print(response.url)
# 查看响应内容，response.text 返回的是文本格式的数据
# print(response.text)
# # 查看响应内容，response.json 返回的是json格式的数据
# print(response.json())