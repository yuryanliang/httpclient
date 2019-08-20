"""
part I

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


part II

In our imaginary world, this client code is to be used by a high-throughput,
multi-threaded web service that needs to fetch exchange rates as fast as possible, potentially in bulk.
Since our imaginary service receives a high volume of traffic,
we want to do this in a way that is very efficient and handles errors properly.
"""
import multiprocessing

import requests


class HTTP_client:
    def __init__(self):
        self.cache={}

    def get_data(self, symbols):
        date = "2017-01-02"
        base = "USD"
        # 1. check cache
        ind = date + base + symbols
        if ind  in self.cache:
            return self.cache[ind]
        else:
            # 2. if not in cache, call API
            url = "https://interview.segment.build/api/rates/{}?base={}&symbols={}".format(date, base, ",".join(symbols))
            response = requests.get(url=url)
            data = response.json()

            # 3. update cache
            ind = date + base + symbols
            value = data
            self.cache[ind]= value
            return data

    def multiprocess(self,symbol_list ):
        with multiprocessing.Pool(processes= 2) as pool:
            pool.map(self.get_data, symbol_list)


if __name__ == "__main__":
    date = "2017-01-02"
    base = "USD"
    symbols_1 = ["EUR", "GBP"]

    # input = date+ base + symbols_1

    # input2

    input_list =[]
    # symbols_2 = ["CAD", "CNY"]
    symbol_list=[symbols_1,symbols_1]


    HTTP_client().multiprocess(symbol_list)
    # data = HTTP_client().get_data(date, base, symbols_1)
    # data = HTTP_client().get_data(date, base, symbols_1)

    # print(data)
