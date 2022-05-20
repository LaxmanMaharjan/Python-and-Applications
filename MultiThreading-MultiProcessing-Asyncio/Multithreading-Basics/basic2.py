import threading
import time

from threading import Thread

def helloworld(k):
    name = threading.current_thread().name
    for _ in range(20):
        print(k)
        print(f"{name} is running\n")
        time.sleep(2)

threads = []

for i in range(10):
    threads.append(Thread(target=helloworld,args=(i,)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
