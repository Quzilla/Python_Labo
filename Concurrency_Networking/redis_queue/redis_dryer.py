import redis, time
conn = redis.Redis()
print('Dryer is starting')
while True:
    time.sleep(20)
    msg = conn.blpop('dishes')
    print(msg)
    if not msg:
        break
    val = msg[1].decode('utf-8')
    if val == 'quit':
        break
    print('Dried', val)
print('Dishes are dried')