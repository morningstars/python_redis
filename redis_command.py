"""

刷新当前数据库  flushdb
刷新所有库  flushall
查看所有key keys *

"""

"""
-------------------  string数据类型  -------------------


# set 设置值
set name zhangsan
set age 20

# get 获取值
get name 
get age

# setnx 键不存在时才能进行设置
setnx name lisi

# set key value ex seconds  多少秒之后删除
set hobby study ex 10

set key value
expire key second
pexpire key milliseconds

# 查看存活时间
ttl key

# 删除过期
persist key

# 获取字符串长度
strlen key

# mset | mget
# 批量设置 | 批量获取

mset key1 value1 key2 value2
mget key1 key2 key3

# 使用冒号 ：作为层级关系
mset zhangsan:email zhangsan@qq.com lisi:email lisi@qq.com
mget zhangsan:email lisi:email


# setrange key 索引值 value
# 替换字符串 从索引值开始 value替换原内容

set message 'hello world'
setrange message 6 'kitty'
get message ->'hello kitty'

setrange message 6 'bb'
get message ->'hello bbtty'

# getrange key 开始索引 结束索引
# 获取指定范围的内容

getrange message 0 2  ->'hel'
getrange message 0 -1  ->'hello bbtty'


# append

set message hello
append message ' world'
get message =>'hello world'

# 整数的操作
incrby key 步长
decrby key 步长
incr key  
decr key
incrbyfloat key 步长

"""

"""
-------------------  通用命令   -------------------

# 切换库
select number

# 查看键
keys *

# 键类型
TYPE key

# 键是否存在
exists key

# 删除键
del key

# 键重命名
rename key newkey

# 返回旧值并设置新值（如果键不存在，就创建并赋值）
getset key value

# 清除当前库中所有数据（慎用）
flushdb

# 清除所有库中所有数据（慎用）
flushall

"""

"""
-------------------  列表数据类型  List  -------------------
元素是字符串类型  列表头尾增删快 中间慢 增删元素是常态
元素可重复
最多包含2^32-1个元素
索引同Python列表


# 头尾压入元素
# LPUSH | RPUSH

LPUSH mylist1 0 1 2 3
RPUSH mylist2 0 1 2 3

# 头尾弹出元素
# LPOP | RPOP

LPOP mylist1
RPOP mylist2

# 从source的尾部pop出元素  push到destination的头部
RPOPLPUSH source destination


# 移除指定元素
# LREM
LREM key count value
# count > 0 表示从头到尾搜索  删除count个value元素
# count < 0 表示从尾到头搜索  删除count个value元素
# count = 0 表示从头到尾搜索  删除所有value元素


# 删除指定范围之外的元素
# LTRIM
LTRIM key start stop

# 列表中插入值
# LINSERT
# value 不存在则不做操作  存在多个则只在第一个value操作
LINSERT key before|after value new_value


# 阻塞弹出
# BLPOP | BRPOP
# 如果列表不存在或为空  会阻塞
# 超时时间为0  永久阻塞 直到有数据可以弹出
# 如果多个客户端阻塞同一个列表  使用FIFS原则 先到先服务
BLPOP key timeout
BRPOP key timeout



# 查看列表元素
# LRANGE key start stop

LRANGE mylist1 0 -1

# 获取指定位置元素
# LINDEX key index

# 设置指定位置的值
# LSET key index element

# 获取列表长度
# LLEN key


"""

"""
-------------------  位图操作  -------------------

# 设置某一位上的值（offset是偏移量，从0开始） 
setbit key offset value

# 获取某一位上的值
getbit key offset

# 统计键所对应的值中有多少个 1
bitcount key

"""

"""
-------------------  哈希 Hash  -------------------

# 1、设置单个字段 
HSET key field value 
HSETNX key field value 

# 2、设置多个字段 
HMSET key field value field value 

# 3、返回字段个数 
HLEN key 

# 4、判断字段是否存在（不存在返回0） 
HEXISTS key field 

# 5、返回字段值 
HGET key field 

# 6、返回多个字段值 
HMGET key field filed 

# 7、返回所有的键值对 
HGETALL key 

# 8、返回所有字段名 
HKEYS key 

# 9、返回所有值 
HVALS key 

# 10、删除指定字段 
HDEL key field 

# 11、在字段对应值上进行整数增量运算 
HINCRBY key filed increment 

# 12、在字段对应值上进行浮点数增量运算 
HINCRBYFLOAT key field increment


"""

"""
-------------------  集合 Set  -------------------


# 1、增加一个或者多个元素,自动去重
SADD key member1 member2
# 2、查看集合中所有元素
SMEMBERS key
# 3、删除一个或者多个元素，元素不存在自动忽略
SREM key member1 member2
# 随机弹出元素 默认为1个
SPOP key [count]

# 4、元素是否存在
SISMEMBER key member
# 5、随机返回集合中指定个数的元素，默认为1个
SRANDMEMBER key [count]
# 6、返回集合中元素的个数，不会遍历整个集合，只是存储在键当中了
SCARD key
# 7、把元素从源集合移动到目标集合
smove scorce destination member 

# 8、差集(number1 1 2 3 number2 1 2 4)
SDIFF key1 key2
# 9、差集保存到另一个集合中
SDIFFSTORE destination key1 key2

# 10、交集
SINTER key1 key2
SINTERSTORE destination key1 key2

# 11、并集
SUNION key1 key2
SUNIONSTORE destionation key1 key2

"""

"""
-------------------  有序集合  sortedset  -------------------

# 在有序集合中添加一个成员 
zadd key score member 

# 查看指定区间元素（升序) 
zrange key start stop [withscores] 
# 查看指定区间元素（降序） 
ZREVRANGE key start stop [withscores] 
# 查看指定元素的分值 
ZSCORE key member 

# 返回指定区间元素
# offset : 跳过多少个元素 
# count : 返回几个 
# 小括号 : 开区间 
zrangebyscore fruits (2.0 8.0 
zrangebyscore key min max [withscores] [limit offset count] 

# 删除成员 
zrem key member 
# 删除指定区间内的元素 
zremrangebyscore key min max

# 增加或者减少分值 
zincrby key increment member 

# 返回元素排名 
zrank key member 
# 返回元素逆序排名 
zrevrank key member 

# 返回集合中元素个数 
zcard key 

# 返回指定范围中元素的个数 
zcount key min max 
zcount fruits 4 7 
zcount fruits (4 7 

# 并集 默认是sum
zunionstore destination numkeys key [weights 权重值] [AGGREGATE SUM|MIN|MAX] 

# 交集：和并集类似，只取相同的元素 
ZINTERSTORE destination numkeys key1 key2 WEIGHTS weight AGGREGATE SUM|MIN|MAX
# 先计算权重 再聚合
zinterstore z_inter 2 z1 z2 weights 0.5 0.3 aggregate max
"""
