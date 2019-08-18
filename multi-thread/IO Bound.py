import threading
import time


def squire(l, res):
    for i in range(len(l)):
        l[i] = l[i] ** 2
        time.sleep(0.5)
    res.append(l)


def main(data):
    st = time.time()
    threads = []
    res = []
    for i in range(4):
        t = threading.Thread(target=squire, args=(data[i], res))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()
    print(res)
    print("thread done,time,", time.time() - st, "\n")


def seq(data):
    st = time.time()
    res = []
    for i in range(4):
        squire(data[i], res)
    print(res)
    print("seq done,time:", time.time() - st, "\n")


if __name__ == '__main__':
    data = [[1, 2, 3], [3, 4, 5], [2, 2, 2], [4, 4, 4]]

    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.main_thread())
    # main(data)
    seq(data)
