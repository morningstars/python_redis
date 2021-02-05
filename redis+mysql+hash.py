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
result = r.hgetall(username)
# redis中查询数据
# 如果查到则直接打印输出
if result:
    print(result)
else:
    # 如果没有查到
    # 从mysql中查询
    print("redis中没有数据")
    sql = 'select gender,age from user where username=%s'
    cursor.execute(sql, [username])
    res = cursor.fetchall()[0]
    print(res)
    if not res:
        print('mysql 无此用户')
    else:
        # 加入redis缓存 设置过期时间为5分钟
        r.hmset(username, {'gender': res[0], 'age': res[1]})
        r.expire(username, 60 * 5)
