import requests
import json

from envVariables import *

r = requests.get("http://api.reimaginebanking.com/merchants?key=" + API_KEY)

i = 0

try:
    while r.json()['data'][i]['geocode'] != "":
        print("lat:" + str(r.json()['data'][i]['geocode']['lat']) + " lng:" + str(r.json()['data'][i]['geocode']['lng']))
        i += 1
except IndexError as e:
    pass
