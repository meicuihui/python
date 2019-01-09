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

    # response = requests.get('https://mp.weixin.qq.com/s/LEkbbxeIV1Z6soKjnDB7Ew',headers=headers)
    response = requests.get('http://www.lzrsks.gov.cn/News/NewsDetailed.aspx?newsId=b4ac00fe5ee04b0f95b9ced6f1f91e8d',headers=headers)
    # response = requests.get('http://2btech.cn/2018/11/05/%E8%AE%A9%20CheckStyle%20%E6%94%AF%E6%8C%81%E5%A2%9E%E9%87%8F%E6%A3%80%E6%9F%A5%E7%9A%84%E4%B8%80%E6%AC%A1%E8%90%BD%E5%9C%B0%E7%BB%8F%E9%AA%8C%E6%80%BB%E7%BB%93/',headers=headers)

    # print(response.text)
    thd.Timer(0.1, fn).start()


fn()
