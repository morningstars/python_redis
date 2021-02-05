import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

# 1. set: 设置 {'mystring':'python'}
r.set('mystring', 'python')

# 2. 获取 mystring 的值,打印查看类型
print(r.get('mystring'))

# 3. 设置 mystring, 当键不存在的时候再设置,存在则不做操作
r.setnx('mystring', 'no value')

# 4. 一次性设置多个键值对,{'mystring2':'mysql','mystring3':'redis'}
r.mset({'mystring2': 'mysql', 'mystring3': 'redis'})

# 5. 一次性获取 三个键 的所有值,查看结果类型?
mget_list = r.mget('mystring', 'mystring2', 'mystring3')
for mget in mget_list:
    print(mget)

# 6. 打印 mystring 的长度
print(r.strlen('mystring'))

# 数字类型操作
r.set('number', 20)
r.incrby('number', 10)
r.decrby('number', 10)

r.incrbyfloat('number', 8.88)
r.incrbyfloat('number', -8.88)

print(r.get('number'))

