"""Here, we have two competing threads in Python that
are each trying to accomplish their own goal of either decrementing the
counter to 1,000, or conversely incrementing it to 10. In a single-core
processor, there is the possibility that worker A manages to complete its task
before worker B has a chance to execute, and the same can be said for worker
B. However, there is a third potential possibility, and that is that the task
scheduler continues to switch between worker A and worker B an infinite
number of times and never completes.

This also shows one of the dangers of multiple
threads accessing shared resources without any form of synchronization.
There is no accurate way to determine what will happen to our counter, and
as such, our program could be considered unreliable"""



from threading import Thread
import time, random

counter = 1

def workerA():
    global counter
    while counter < 10:
        counter += 1
        print(f"workerA is incrementing counter to {counter}")
        time.sleep(random.randint(0,1))

def workerB():
    global counter
    while counter > -10:
        counter -= 1
        print(f"workerB is incrementing counter to {counter}")
        time.sleep(random.randint(0,1))

start = time.time()
t1 = Thread(target=workerA)
t2 = Thread(target=workerB)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()
print(f"Execution Time {end-start}")

