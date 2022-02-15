import json
import time

from requests import Session, Response

from utils import http

base_url = "https://heapdump.cn/api/"


def response_post(response: Response):
    if response.status_code != 200:
        print("接口异常", response.text)
        raise Exception("接口异常")
    else:
        if not response.json()["status"]:
            if response.json()["code"] == 500:
                print("接口系统500异常", response.text)
                raise Exception("接口系统500异常")
            if response.json()["code"] == 500:
                print("接口业务异常", response.text)
    return response.json()


def default_heapdump(func):
    def inner(*a, **b):
        start = time.time()
        response: Response = func(*a, **b)
        end = time.time()
        print("执行时间%s" % (end - start), "结果值：", response.text)
        if response.status_code == 401:
            print("Cookie过期，未登录", response.text)
            service_ticket = login()
            a[0].cookies.set("serviceTicket", service_ticket)
            response: Response = func(*a, **b)
        return response_post(response)

    return inner


def session():
    return http.session()


def login():
    url = base_url + "login/authentication/v1/login"
    para = json.dumps({
        "account": "13776573557",
        "passwd": "1dd6c550919cc8cd97a556545f27e3f8d87aac77eac80747aeeca97781dd5044853fce04d69060e1c5c2bb31d9e93aaf399d1d7ecf52a9f49fb5e30358722fba"
    })
    response: Response = http.post(url, para)
    return response.cookies.get("serviceTicket")


# ====================== session ======================
@default_heapdump
def add_signin(s: Session, **keys):
    url = base_url + "community/signin/addSignin"
    return http.session_post(s, url, **keys)


@default_heapdump
def current_month_sigin(s: Session):
    url = base_url + "community/signin/currentMonthSigin"
    return http.session_get(s, url)


@default_heapdump
def is_signin(s: Session):
    url = base_url + "community/signin/isSignin"
    return http.session_get(s, url)


@default_heapdump
def new_list(s: Session, page=1, size=10):
    url = base_url + "community/newList?page=" + str(page) + "&size=" + str(size) + "&sort=0&labels="
    return http.session_get(s, url)


@default_heapdump
def add_like(s: Session, post_id):
    url = base_url + "community/post/like"
    json_par = json.dumps({"postId": post_id})
    return http.session_post(s, url, data=json_par)


@default_heapdump
def discuss(s: Session, ref_id, content):
    url = base_url + "community/post/discuss"
    json_par = json.dumps({
        "refId": ref_id,
        "content": content,
        "type": 1,
        "parentReplyId": 0
    })
    return http.session_post(s, url, data=json_par)


login()
