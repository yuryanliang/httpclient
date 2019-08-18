import threading
import time


def count_n(x, who):
    print("Start count: ", x, who,"\n")
    for i in range(20000000):
        x +=1
    print("Done", who, ". result is ", x,"\n")
    return x


def main():
    st = time.time()

    print("thread start")
    thread1 = threading.Thread(target=count_n,args=(0,"thread") )
    thread2 = threading.Thread(target=count_n, args=(1,"thread"))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("thread done,time,", time.time()-st,"\n")
def seq():
    st = time.time()

    print("seq start")
    count_n(0, "seq")
    count_n(1, "seq")
    print("seq done,time,", time.time()-st,"\n")


if __name__ == '__main__':
    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.main_thread())
    main()
    # seq()

