import time
from multiprocessing import Pool
import requests


def get_data(url):
    r1 = requests.get(url)
    print("Read {} from {}".format(len(r1.content), url) )

def all(sites):
    with Pool(8) as p:
        p.map(get_data, sites)
    # for url in sites:
    #     get_data(url)



if __name__ == '__main__':
    sites =[
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] *40
    start_time =time.time()
    all(sites)
    print("time duration: {}".format(time.time()-start_time))
    # with Pool(5) as p:
    #     print(p.map(get_data, terms))

