from time import sleep, time

t1 = time()
num = 5
num *= 2
print(time() - t1)

sleep(1.0)
print(time() - t1)