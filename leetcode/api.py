import time

from requests import Session, Response

from utils import http

base_url = "https://leetcode.cn/"


def response_post(response: Response):
    if response.status_code != 200:
        print("接口异常", response.text)
        raise Exception("接口异常")
    else:
        return response


def default_leetcode(func):
    def inner(*a, **b):
        start = time.time()
        response: Response = func(*a, **b)
        end = time.time()
        print("执行时间%s" % (end - start), "结果值：", response.text)
        if response.status_code == 401:
            print("Cookie过期，未登录", response.text)
        return response_post(response)

    return inner


def session():
    return http.session()


# ====================== session ======================


@default_leetcode
def points_total(s: Session):
    url = base_url + "points/api/total/"
    return http.session_get(s, url)
