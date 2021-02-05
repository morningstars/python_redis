import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

r.setbit('user1', 0, 1)
r.setbit('user1', 4, 1)

r.setbit('user2', 99, 1)
r.setbit('user2', 199, 1)

for i in range(1, 365, 2):
    r.setbit('user3', i, 1)

for i in range(1, 365, 3):
    r.setbit('user4', i, 1)


userlist = r.keys('user*')
print(userlist)

activeuser= []
noactiveuser= []

for user in userlist:
    logincount = r.bitcount(user.decode())
    if logincount > 100:
        activeuser.append((user, logincount))
    else:
        noactiveuser.append((user, logincount))

print(activeuser)
print(noactiveuser)