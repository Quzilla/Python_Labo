import threading, queue
import time
print(__name__)

def washer (dishes, dish_queue):
    for dish in dishes:
        print('Washin', dish)
        time.sleep(5)
        dish_queue.put(dish)
        
def dryer(dish_queue):
    while True:
        print("wait...")
        # ここでキューが入ってくるのを待機している。初回は sarada
        dish = dish_queue.get()
        print('Drying', dish)
        time.sleep(10)
        dish_queue.task_done()

dish_queue = queue.Queue()
for n in range(2):
    dryer_thread = threading.Thread(target=dryer, args=(dish_queue,))
    dryer_thread.start()
    
dishes = ['sarada', 'bread', 'entree', 'desert']
washer(dishes, dish_queue)
dish_queue.join()
print('end')