import requests
import threading as thd
import time


def fn():
    print(time.time())
    headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
    "Accept-Encoding":"gzip",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Referer":"http://www.example.com/",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36" }

    response = requests.get('',headers=headers)

    # print(response.text)
    thd.Timer(0.1, fn).start()


fn()
