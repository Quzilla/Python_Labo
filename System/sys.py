def aaa ():
    from datetime import date
    import time
    with open('today.txt', 'wt') as f:
        now = date.today().isoformat()
        f.write(now)
        
    with open('today.txt', 'rt') as f:
        today_string = f.read()
        fmt = "%Y-%m-%d"
        fm =time.strptime(today_string, fmt)
        print(fm)
  
def bbb():
    import os
    print(os.listdir('.'))
    print(os.listdir("../"))

def ccc():
    import os, subprocess, multiprocessing, time
    from random import randint
    # print(subprocess.getoutput('date'))
    # print(subprocess.check_output(['date','-u']))
    
    
    def test_do(i):
        print("{} hey: {}".format(os.getpid(), i))
    def test_call(i):
        test_do(i)

    if __name__ == "__main__":
        print(os.getpid())
        for i in range(3):
            p = multiprocessing.Process(target=test_call, args=(i,))
            p.start()
            time.sleep(randint(1,5))
        print("end")
        
import datetime
birthday = datetime.date(1997,7,23)
print(type(birthday))
print(birthday.weekday())
party = birthday + datetime.timedelta(days=1000)
print(party)