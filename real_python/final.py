import multiprocessing
import time

import requests


def download_site(url):
    s = requests.Session()
    s.auth = ('user', 'pass')
    s.headers.update({'x-test': 'true'})

    # both 'x-test' and 'x-test2' are sent
    s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})

    header = {
        "username": "user",
        "password": "password",
    }
    param ={
        "param":"something"
    }

    try:
        response = requests.get(url, timeout=3, headers=header, params=param)
        if response.status_code == 200:
            print("Read: {}, from {}".format(len(response.content), url))
        else:
            print("no good response")
    except ConnectionError as e:
        print(e.message)


def download_all_sites(sites):
    with multiprocessing.Pool(processes=5) as pool:
        pool.map(download_site, sites)
    # for i,url in enumerate(sites):
    #     print(i)
    #     download_site(url)


if __name__ == "__main__":
    sites = [
                "https://www.jython.org",
                "http://olympus.realpython.org/dice",
            ] * 40

    start_time = time.time()
    download_all_sites(sites)
    print("Duration: {}".format(time.time() - start_time))
