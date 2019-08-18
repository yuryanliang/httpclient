import threading


def job1():
    global x, lock
    lock.acquire()
    for i in range(10):
        x += 1
        print(threading.current_thread(), x)
    lock.release()


def job2():
    global x, lock
    lock.acquire()
    for i in range(10):
        x += 10
        print(threading.current_thread(), x)
    lock.release()


if __name__ == '__main__':
    lock = threading.Lock()
    x = 0
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("final x:", x)  # some time x is 5 and other time x is 10
