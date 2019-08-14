# importing the requests library
import json

import requests

# # api-endpoint
# URL = "http://maps.googleapis.com/maps/api/geocode/json"
#
# # location given here
# location = "delhi technological university"
#
# # defining a params dict for the parameters to be sent to the API
# PARAMS = {'address':location}
#
# # sending get request and saving the response as response object
# r = requests.get(url = URL, params = PARAMS)
#
# # extracting data in json format
# data = r.json()
#
#
# # extracting latitude, longitude and formatted address
# # of the first matching location
# latitude = data['results'][0]['geometry']['location']['lat']
# longitude = data['results'][0]['geometry']['location']['lng']
# formatted_address = data['results'][0]['formatted_address']
#
# # printing the output
# print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
# 	%(latitude, longitude,formatted_address))


def Get_request():
	url = "https://jsonplaceholder.typicode.com/posts/"

	location = "delhi technological university"

	params = {
		'address': location
	}

	r = requests.get(url = url)

	data = r.json()
	d = json.loads(r.content)
	1==1

def Post_request():


	# defining the api-endpoint
	API_ENDPOINT = "http://pastebin.com/api/api_post.php"

	# your API key here
	API_KEY = "XXXXXXXXXXXXXXXXX"

	# your source code here
	source_code = ''' 
	print("Hello, world!") 
	a = 1 
	b = 2 
	print(a + b) 
	'''

	# data to be sent to api
	data = {'api_dev_key': API_KEY,
			'api_option': 'paste',
			'api_paste_code': source_code,
			'api_paste_format': 'python'}

	# sending post request and saving response as response object
	r = requests.post(url=API_ENDPOINT, data=data)

	# extracting response text
	pastebin_url = r.text
	print("The pastebin URL is:%s" % pastebin_url)


if __name__ == '__main__':
	# Get_request()
	Post_request()
