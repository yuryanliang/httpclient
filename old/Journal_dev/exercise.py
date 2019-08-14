
import http.client

# connection = http.client.HTTPConnection('www.python.org', 80, timeout=10)
# print(connection)
import requests

connection = http.client.HTTPConnection(host='www.python.org', port=80, timeout=10)
print(connection)

import http.client
import pprint

connection = http.client.HTTPSConnection("www.journaldev.com")
connection.request("GET", "/")
response = connection.getresponse()
headers = response.getheaders()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint("Headers: {}".format(headers))


import http.client

connection = http.client.HTTPSConnection("www.python.org")

r=connection.request("GET", "/")
response = connection.getresponse()
print("Status: {} and reason: {}".format(response.status, response.reason))

connection.close()



