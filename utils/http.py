import logging

import requests


def session():
    return requests.session()


def http(method, url, data, **keys):
    response = {}
    if method == "POST":
        response = requests.post(url, data, **keys)
    elif method == "GET":
        response = requests.get(url, data, **keys)
    return response


def get(url, data, **keys):
    response = requests.get(url, data, **keys)
    if response.status_code != 200:
        logging.error("接口异常", response)
        raise Exception("接口异常")
    return response


def post(url, data, **keys):
    response = requests.post(url, data, **keys)
    if response.status_code != 200:
        logging.error("接口异常", response)
        raise Exception("接口异常")
    return response
