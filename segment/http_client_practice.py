"""
The goal is to write reusable client code that can be used to access an HTTP API that returns currency exchange rates in JSON format.
 Note that the exchange rates at a specified date are immutable: the same request would always return the same response.

This API is live on the internet and can be accessed using a GET request to a URL formatted like
https://interview.segment.build/api/rates/<date>?base=<base>&symbols=<symbol>
where <base>  is a currency code (e.g. USD for US dollars, EUR for Euro, and GBP for British Pound),
<symbol> is a comma-delimited list of the currency codes we want to compare against the base and <date> is the date.

An example request using the curl command:
$ curl -s 'https://interview.segment.build/api/rates/2017-01-02?base=USD&symbols=EUR,GBP'
{
  "Base": "USD",
  "Date": "2017-01-02",
  "Rates": {
    "EUR": 0.95557,
    "GBP": 0.81357
  }
}
"""
import sys

import requests


class exchange_client:
    def __init__(self, date, base, symbols):
        self.date = date
        self.base = base
        self.symbols = symbols

    def get_data(self):
        url = "https://interview.segment.build/api/rates/{}?base={}&symbols={}".format(self.date, self.base,
                                                                                       ",".join(symbols))

        response = requests.get(url=url)
        data = response.json()
        size = sys.getsizeof(data)
        # 248 * 365*10*100/1024/1024 = 86 Mb
        return data


# @classmethod
# def get_cache

class ExchangeRateClient:
    def __init__(self):
        self.cache = {}

        # cache
        # size =sys.getsizeof(data)
        # 248 * 365*10*100/1024/1024 = 86 Mb

        # no need to LRU or LFU

    def get_rate(self, date, base, symbols):
        result = {}
        new_symbols=[]

        for symbol in symbols:
            ind = date + "+" + base + "-" + symbol
            if ind in self.cache:
                result[ind] = self.cache[ind]
            else:
                new_symbols.append(symbol)

        # 1. see if request already in cache
        # ind = date + "+" + base + ":" + "-".join(symbols)
        # if ind in self.cache:
        #     return self.cache[ind]
        # else:

        if new_symbols:

            # 2. api
            url = "https://interview.segment.build/api/rates/{}?base={}&symbols={}".format(date, base,
                                                                                           ",".join(new_symbols))
            try:
                response = requests.get(url=url, timeout=10)
                response.raise_for_status()
            except requests.exceptions.ConnectionError as e:
                # DNS failure, refused connection
                print(e.args[0].reason.args[0])
                sys.exit(1)

            except requests.exceptions.Timeout as e:
                print("Time out:", e)
                sys.exit(1)

            # Maybe set up for a retry, or continue in a retry loop
            except requests.exceptions.HTTPError as e:
                # there is a non-200 error
                # currency error. date error
                print("Status code is non-200:", e.response.text)
                sys.exit(1)

            # if want to do retry:
            #     from requests.adapters import HTTPAdapter
            #
            #     s = requests.Session()
            #     s.mount('http://stackoverflow.com', HTTPAdapter(max_retries=5))

            # 3. update cache
            data = response.json()
            for symbol, rate in data["Rates"].items():
                ind = date + "+" + base + "-" + symbol
                result[ind]=rate
                self.cache[ind] = rate

        return result
""" base + symbol
            for symbol, rate in data["Rates"].items():
                ind = base + "-" + symbol
                if ind not in self.cache:
                    self.cache[ind] = {date: rate}
                else:
                    if date not in self.cache[ind]:
                        self.cache[ind].update({date: rate})
"""

if __name__ == "__main__":
    date_1 = "2007-01-02"
    base = "USD"
    symbols = ["EUR"]

    client = ExchangeRateClient()

    rate = client.get_rate(date_1, base, symbols)
    date_2 = "2007-01-02"
    symbols = ["EUR", "GBP"]
    rate_2 = client.get_rate(date_2, base, symbols)
    print(rate_2)
