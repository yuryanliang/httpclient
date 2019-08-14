import time
from multiprocessing import Pool


def doubler(number):
    print(1)
    time.sleep(1)
    print(str(2)+"\n")

    return number * 2


if __name__ == '__main__':
    numbers = [5, 10, 20,9]
    pool = Pool(processes=3)
    print(pool.map(doubler, numbers))