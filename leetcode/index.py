import random
import time

from leetcode import api


def auto():
    session = api.session()
    session.cookies.set("serviceTicket", "e7ae53b20fc240e1a18555fbc3cce680")
    i = random.randrange(1, 100)
    time.sleep(i)
    api.points_total(session)


def test():
    session = api.session()
    session.cookies.set("LEETCODE_SESSION",
                        "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuZXh0X2FmdGVyX29hdXRoIjoiL3Byb2ZpbGUvYWNjb3VudC8iLCJfYXV0aF91c2VyX2lkIjoiMTAzMjczNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzExOGMyMzUyYjhlNWU1MDA4NzJmODZkMGFkZmZjMDMzNjQzZTEwNDYyMzg1ZGNjOTg5ZGZiOTJlNzcyZTY4YiIsImlkIjoxMDMyNzM3LCJlbWFpbCI6IjQ1MjQyNTk1MkBxcS5jb20iLCJ1c2VybmFtZSI6Inp1aS1wYS1kZS1xaS1zaGktc2hpLWd1LWRhbiIsInVzZXJfc2x1ZyI6Inp1aS1wYS1kZS1xaS1zaGktc2hpLWd1LWRhbiIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNuL2FsaXl1bi1sYy11cGxvYWQvdXNlcnMvenVpLXBhLWRlLXFpLXNoaS1zaGktZ3UtZGFuL2F2YXRhcl8xNTc0NDEyMzY3LnBuZyIsInBob25lX3ZlcmlmaWVkIjpmYWxzZSwiX3RpbWVzdGFtcCI6MTY1ODMyNTQ0MC40MjU3MDE2LCJleHBpcmVkX3RpbWVfIjoxNjYwODQ5MjAwLCJ2ZXJzaW9uX2tleV8iOjAsImxhdGVzdF90aW1lc3RhbXBfIjoxNjU4MzI1NTY0fQ.ndmH6sr818BtpQGQyX3eH0WSasK2vFAzkNmzzlhubHY")
    r = api.points_total(session)
    print(r)
