import threading
import time

def helloworld(k):
    name = threading.current_thread().name
    for _ in range(10):
        print(k)
        print(f"{name} is running\n")
        time.sleep(2)

t1 = threading.Thread(target=helloworld, args=(1,))
t2 = threading.Thread( target=helloworld, args=(2,))

t1.start()
t2.start()
t1.join()
t2.join()
