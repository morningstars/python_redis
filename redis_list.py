import redis

r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    db=0
)

# print(r.keys('*'))
#
# print(r.exists('name'))
#
# print(r.lrange('spider::urls', 0, -1))

r.delete('tedu:python')

# lpush rpush命令 ['pythonweb','socket','spiderman']
r.lpush('tedu:python', 'pythonweb', 'socket', 'spiderman')

# 查看:[b'pythonweb', b'socket', b'spiderman']
print(r.lrange('tedu:python', 0, -1))

# 从列表尾部弹出1个元素
r.rpop('tedu:python')

# 从列表头部弹出1个元素
r.lpop('tedu:python')

# 列表尾部插入3个元素 [b'socket','mysql','mongodb','oracle']
r.rpush('tedu:python', 'mysql', 'mangodb', 'oracle')

# 删除索引为2的元素 [b'socket','mysql','oracle']
index_2 = r.lindex('tedu:python', 2)
r.lrem('tedu:python', 1, index_2.decode())

# 保留列表中的前2个元素 [b'socket','mysql']
r.ltrim('tedu:python', 0, 1)

# 把下表索引为0的元素设置为: redis [b'redis','AI','mysql']
r.lset('tedu:python', 0, 'redis')

# 在redis元素的后面插入1个元素: AI
r.linsert('tedu:python', 'after', 'redis', 'AI')

# 获取列表长度
print(r.llen('tedu:python'))

# 删除tedu:python



