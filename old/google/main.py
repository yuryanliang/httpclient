import requests,json,time
def google():
    searchTerms = input("shenyang, beijing")

    start_time = time.time() #timer
    searchTerms = searchTerms.split(',')
    for i in searchTerms:
        r1 = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?query='+ i +'&key=MY_KEY')
        a = r1.json()
        pid = a['results'][0]['place_id']
        r2 = requests.get('https://maps.googleapis.com/maps/api/place/details/json?placeid='+pid+'&key=MY_KEY')
        b = r2.json()
        phone = b['result']['formatted_phone_number']
        name = b['result']['name']
        website = b['result']['website']
        print(phone+' '+name+' '+website)

    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print(time.time()- start_time)

    start_time = time.time()
    print(time.time()-start_time)

