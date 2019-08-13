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
class HTTP_client:



    def get_data(self, date, base, symbols):
        url ="https://interview.segment.build/api/rates/{}?base={}&symbols={}".format(self.date, self.base, ",".join(symbols))

        response = requests.get(url=url)
        data = response.json()
        sys.getsizeof (data)
        return data




if __name__=="__main__":
    date = "2017-01-02"
    base = "USD"
    symbols = ["EUR", "GBP"]
    lookup ={}
    ind = date + base + "".join(symbols)

    lookup[ind]= HTTP_client().get_data(date, base, symbols)





    url = "https://interview.segment.build/api/rates/2017-01-02?base=USD&symbols=EUR,GBP"