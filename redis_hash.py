import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

r.hset('student', 'name', 'Lucy')

r.hset('student', 'age', 18)

r.hset('student', 'score', 98)

r.hmset('student', {'gender': 'm', 'class': '1903', 'hobby': 'study'})

print(r.hget('student', 'name'))
print(r.hmget('student', 'name', 'class'))

print(r.hgetall('student'))

print(r.hkeys('student'))

print(r.hvals('student'))

print(r.hlen('student'))

print(r.hexists('student', 'hello'))
print(r.hexists('student', 'class'))

r.hdel('student', 'hobby')
