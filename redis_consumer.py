"""
从xiaomi:urls中获取url地址 进行数据抓取
"""

import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

while True:
    # 从列表中获取地址
    # (b'xiaomi:urls', b'http://app.mi.com/#page=1')
    # none

    url = r.brpop('xiaomi:urls', 6)
    if url:
        print(url[1].decode())
        print('抓取中。。。')
    else:
        print('抓取结束')
        break
