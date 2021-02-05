
'''

# 安装redis
brew install redis

默认端口  6379

# 启动redis
brew services start redis

# redis配置文件的路径
/usr/local/etc/redis.conf

# 设置密码为123456
修改redis.conf中 requirepass 为123456
需要重启服务

# 注释掉本地ip地址绑定
# 127.0.0.1 ::1

# 关闭保护模式
protected-mode 改为no
需要重启服务

# 启动redis客户端
redis-cli

# 启动redis客户端 需要输入密码
redis-cli -a 123456


# 连接成功
输入 ping  返回pong



'''
