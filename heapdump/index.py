# import requests
# import json
#
# url = "https://heapdump.cn/api/login/authentication/v1/login"
# para = {
#   "account": "13776573557",
#   "passwd": "1dd6c550919cc8cd97a556545f27e3f8d87aac77eac80747aeeca97781dd5044853fce04d69060e1c5c2bb31d9e93aaf399d1d7ecf52a9f49fb5e30358722fba"
# }
# header = {"Content-Type": "application/json"}
# #python数据类型转换为json类型（json.dumps()）
# para = json.dumps(para)
# # r = requests.post(url, para, header)
# r = requests.post(url, headers=header, data=para)
#
# print('post请求获取的响应结果json类型', r.text)
# print("post请求获取响应状态码", r.status_code)
# print("post请求获取响应头", r.headers['Content-Type'])
#
# #响应的json数据转换为可被python识别的数据类型
# json_r = r.json()
# print("post请求获取响应结果值", json_r)
# print(r.cookies)
#
# # r1 = requests.get("https://heapdump.cn/api/community/signin/isSignin", cookies=r.cookies)
# # print('post请求获取的响应结果json类型', r1.text)
# # print("post请求获取响应状态码", r1.status_code)
# # print("post请求获取响应头", r1.headers['Content-Type'])
# #
# # #响应的json数据转换为可被python识别的数据类型
# # json_r = r1.json()
# # print("post请求获取响应结果值", json_r)
# # print(r1.cookies)
#
#
# r1 = requests.post("https://heapdump.cn/api/community/signin/addSignin", headers=header, cookies=r.cookies)
# print('post请求获取的响应结果json类型', r1.text)
# print("post请求获取响应状态码", r1.status_code)
# print("post请求获取响应头", r1.headers['Content-Type'])
#
# #响应的json数据转换为可被python识别的数据类型
# json_r = r1.json()
# print("post请求获取响应结果值", json_r)
# print(r1.cookies)
#
#
from heapdump import api


def auto():
    # session = api.session()
    data = {
      "account": "13776573557",
      "passwd": "1dd6c550919cc8cd97a556545f27e3f8d87aac77eac80747aeeca97781dd5044853fce04d69060e1c5c2bb31d9e93aaf399d1d7ecf52a9f49fb5e30358722fba"
    }
    login_response = api.login(data)
    print(login_response.json())
    add_signin_response = api.add_signin(login_response.cookies)
    print(add_signin_response.json())

