import redis

r = redis.Redis(host='localhost', port=6379, db=0)

r.sadd('user_one', 'tom', 'jim', 'tim')
r.sadd('user_two', 'tom', 'jim', 'lim')

res = r.sinter('user_one', 'user_two')
print(res)
print(type(res))

s = set()
for r in res:
    s.add(r.decode())

print(s)

# print(r.scard('set_name'))
#
# r.srem('set_name', 'h')
