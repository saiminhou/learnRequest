import requests
from requests.auth import HTTPBasicAuth

url = 'https://api.github.com/octocat'
headers = {
"X-GitHub-Api-Version": "2022-11-28"
}
resp = requests.get(url, auth=HTTPBasicAuth('1367295926@qq.com', 'password'),headers=headers)
from requests.auth import HTTPDigestAuth

url = 'https://httpbin.org/digest-auth/auth/user/pass'

resp = requests.get(url, auth=HTTPDigestAuth('user', 'pass'))

import requests
from requests_oauthlib import OAuth1
oauth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
response = requests.get('http://example.com/api', auth=oauth)

from requests_oauthlib import OAuth2Session

client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
redirect_uri = 'YOUR_REDIRECT_URI'
authorization_base_url = 'https://example.com/oauth/authorize'
token_url = 'https://example.com/oauth/token'


def token_updater(token):
    """存储Token"""
    pass


def authorization():
    """用户授权"""
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)
    authorization_url, state = oauth.authorization_url(authorization_base_url)
    print('请点击以下链接进行授权：', authorization_url)
    authorization_response = input('请输入授权后返回的地址：')
    token = oauth.fetch_token(token_url, authorization_response=authorization_response, client_secret=client_secret,
                              include_client_id=True, method='POST',
                              headers={'Authorization': 'Basic ' + client_secret})
    token_updater(token)
    return token


def api_call():
    """调用API"""
    oauth = OAuth2Session(client_id, token=token_updater())
    response = oauth.get('https://example.com/api')
    return response.json()