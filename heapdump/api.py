import json

from utils import http


def session():
    return http.session()


def login(data, header=None):
    if header is None:
        header = {"Content-Type": "application/json"}
    url = "https://heapdump.cn/api/login/authentication/v1/login"
    # python数据类型转换为json类型（json.dumps()）
    para = json.dumps(data)
    return http.post(url, para, headers=header)


def add_signin(cookies, header=None):
    if header is None:
        header = {"Content-Type": "application/json"}
    url = "https://heapdump.cn/api/community/signin/addSignin"
    return http.post(url, {}, headers=header, cookies=cookies)
