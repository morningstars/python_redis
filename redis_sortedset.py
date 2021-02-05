import redis

r = redis.Redis(host='localhost', port=6379, db=0)

r.zadd('ranking', {'song1': 1, 'song2': 1, 'song3': 1})
r.zadd('ranking', {'song4': 1, 'song5': 1})
r.zadd('ranking', {'song6': 1, 'song7': 1, 'song8': 1})

r.zincrby('ranking', 50, 'song3')
r.zincrby('ranking', 60, 'song5')
r.zincrby('ranking', 70, 'song7')

# 获取前3名
rlist = r.zrevrange('ranking', 0, 2, withscores=True)
print(rlist)

i = 1
for rs in rlist:
    print('第{}名：{}, 播放量：{}'.format(i, rs[0].decode(), int(rs[1])))
    i += 1


# 并集
day01_dict = {
    'huawei': 5000,
    'oppo': 3000,
    'iphone': 1000
}

day02_dict = {
    'huawei': 5500,
    'oppo': 3500,
    'iphone': 1500
}

day03_dict = {
    'huawei': 5900,
    'oppo': 3900,
    'iphone': 1900
}

r.zadd('mobile-day01', day01_dict)
r.zadd('mobile-day02', day02_dict)
r.zadd('mobile-day03', day03_dict)

r.zunionstore('mobile-day01:03',
              ('mobile-day01', 'mobile-day02', 'mobile-day03'),
              aggregate='max'
              )
rlist = r.zrevrange('mobile-day01:03', 0, -1, withscores=True)
print(rlist)

i = 1
for r in rlist:
    print('第{}名：{}, 数量：{}'.format(i, r[0].decode(), int(r[1])))
    i += 1





