import requests
import multiprocessing
import time


def get_data(url):
    response = requests.get(url)
    print("Read: {}, url: {}".format(len(response.content), url))


def multiple_data(url_list):
    # with multiprocessing.Pool(5) as pool:
    #     pool.map(get_data, url_list)
    for url in url_list:
        get_data(url)


if __name__ == "__main__":
    url_list = [
                   "https://www.jython.org",
                   "http://olympus.realpython.org/dice",
               ] * 40
    start_time = time.time()
    multiple_data(url_list)
    print("Duration: {}".format(time.time() - start_time))
