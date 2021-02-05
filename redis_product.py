import random
import time

import redis

r = redis.Redis(host='127.0.0.1',
                port=6379,
                db=0)

for i in range(1, 20):
    url = 'http://app.mi.com/#page=' + str(i)
    r.lpush('xiaomi:urls', url)
    time.sleep(random.randint(3, 5))
