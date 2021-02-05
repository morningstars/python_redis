# 1、到redis缓存中查询个人信息
# 2、redis中查询不到，到mysql查询，并缓存到redis
# 3、再次查询个人信息

import redis
import pymysql

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

db = pymysql.connect('localhost', 'root', '123456', 'userdb', charset='utf8')
cursor = db.cursor()

# 输入用户名
username = input("输入用户名：")
age = input('请输入年龄：')

# 改sql数据库
sql = 'update user set age=%s where username=%s'
cursor.execute(sql, [age, username])
db.commit()

# 同步到redis数据库
r.hset(username, 'age', age)
r.expire(username, 60 * 5)

print(r.hget(username, 'age'))
