import requests

# 创建一个session对象
s = requests.session()
print("会话初始cookies：", dict(s.cookies))
# 第一次请求
r1 = s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')

print("第一次请求后，会话现有cookies：", dict(s.cookies))
# 第二次请求
r2 = s.get('http://httpbin.org/cookies')
print("第二次请求后，会话现有cookies：", dict(s.cookies))