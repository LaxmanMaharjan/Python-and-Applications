from threading import Thread
import time, random, threading

counter = 1
lock = threading.Lock()

def workerA():
    global counter
    lock.acquire()
    try:
        while counter < 10:
            counter += 1
            print(f"WorkerA incremented counter to {counter}")
            time.sleep(random.randint(0,1))
    finally:
        lock.release()

def workerB():
    global counter
    lock.acquire()
    try:
        while counter > -10:
            counter -= 1
            print(f"WorkerB decremented counter to {counter}")
            time.sleep(random.randint(0,1))
    finally:
        lock.release()

start = time.time()
t1 = Thread(target=workerA)
t2 = Thread(target=workerB)

t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print(f'Execution Time is {end-start}')
