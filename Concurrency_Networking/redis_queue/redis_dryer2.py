def dryer():
    import redis, time, os
    conn = redis.Redis()
    pid = os.getpid()
    timeout = 20
    print('Dryer process {} is starting'.format(pid))
    while True:
        msg = conn.blpop('dishes', timeout=timeout)
        print(msg)
        if not msg:
            break
        val = msg[1].decode('utf-8')
        if val == 'quit':
            break
        print('{0}: dried {1}'.format(pid, val))
        time.sleep(0.1)
    print('Dryer process {} is done'.format(pid))
    
if __name__ == "__main__":
    import multiprocessing
    DRYERS = 3
    for num in range(DRYERS):
        p = multiprocessing.Process(target=dryer)
        p.start()