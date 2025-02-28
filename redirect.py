
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}

r = requests.get("http://www.360buy.com", headers=headers,allow_redirects=False)

print("历史请求过程信息：")
print(r.history)
for one_info in r.history:
    print(one_info.status_code, one_info.url, one_info.headers)

print("\n\n最后一次的请求信息：")
print(r.status_code, r.url, r.headers)