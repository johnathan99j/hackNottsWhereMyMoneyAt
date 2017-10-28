import requests
import json

from envVariables import *

# print ("Hi You")

r = requests.get("http://api.reimaginebanking.com/merchants?key=" + API_KEY)

print (r.content)

# parsed_json = json.loads(r.json())

# print(r.json()['geocode'])

def parseGPS(arg):
    pass
