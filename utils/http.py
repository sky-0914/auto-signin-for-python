import requests
from requests import Session


def default_header(func):
    def inner(*a, **b):
        if "headers" not in b:
            b["headers"] = {"Content-Type": "application/json"}
        return func(*a, **b)

    return inner


def session():
    return requests.session()


@default_header
def get(url, data, **keys):
    return requests.get(url, data, **keys)


@default_header
def post(url, data, **keys):
    return requests.post(url, data, **keys)


@default_header
def delete(url, data, **keys):
    return requests.delete(url, data, **keys)


@default_header
def session_get(s: Session, url, **keys):
    return s.get(url, **keys)


@default_header
def session_post(s: Session, url, **keys):
    return s.post(url, **keys)


@default_header
def session_delete(s: Session, url, **keys):
    return s.delete(url, **keys)
