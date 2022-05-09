def current_time_fle():
    from datetime import date
    import time
    with open('today.txt', 'wt') as f:
        now = date.today().isoformat()
        f.write(now)
        
    with open('today.txt', 'rt') as f:
        today_string = f.read()
        print(today_string)
        
        fmt = "%Y-%m-%d"
        fm =time.strptime(today_string, fmt)
        print(fm)
  
def dir_list():
    import os
    print(os.listdir('./'))
    print(os.listdir("../"))
        
def calc_birthday():
    import datetime
    birthday = datetime.date(1997,7,23)
    print(birthday.weekday())
    party = birthday + datetime.timedelta(days=1000)
    print(party)
    
def now_for_multiprocessing(seconds):
    from datetime import datetime
    from time import sleep
    sleep(seconds)
    print('wait', seconds, 'seconds time is', datetime.utcnow())
    
if __name__ == "__main__":
    current_time_fle()
    dir()
    calc_birthday()
    
    import multiprocessing
    import random
    for n in range(3):
        seconds = random.random()
        proc = multiprocessing.Process(target=now_for_multiprocessing, args=(seconds,))
        proc.start()