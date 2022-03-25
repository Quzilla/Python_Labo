import multiprocessing as mp 
import time

# サブプロセスがコードを見にくるのを確認
print(__name__)

def washer(dishes, output):
    for dish in dishes:
        print('Washing', dish, 'dish')
        output.put(dish)
        time.sleep(2)
        
def dryer(input):
    while True:
        dish = input.get()
        print('Drying', dish, 'dish')
        input.task_done()


if __name__ == '__main__':
    dish_queue = mp.JoinableQueue()
    dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
    dryer_proc.daemon = True
    dryer_proc.start()

    dishes = ['sarada', 'bread', 'entree', 'dessert']
    washer(dishes=dishes, output=dish_queue)
    dish_queue.join()
    print('end')