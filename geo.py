#!/usr/bin/python
import requests
import json
import sys

from envVariables import *

def main():
    i, j = 0, 0

    # cust id -> account(s) id -> purchase(s) id -> merchant id -> gps
    # custId = "59f45071a73e4942cdafe49f"

    if len(sys.argv) != 2:
        exit("Error: Must pass customer id as first and only arguemnt")

    custId = sys.argv[1]

    file = open("capital_one_open_bank/static/GeoJSONP.js","w")

    file.write('eqfeed_callback({"type": "FeatureCollection","features": [')

    r = requests.get("http://api.reimaginebanking.com/customers/" + custId + "/accounts?key=" + API_KEY)

    try:
        # Loop though all the customers accounts
        while r.json()[i]['_id'] != "":
            s = requests.get("http://api.reimaginebanking.com/accounts/" + str(r.json()[i]['_id']) + "/purchases?key=" + API_KEY)

            # Loop though all the purchases in this account
            while s.json()[j]['merchant_id'] != "":
                t = requests.get("http://api.reimaginebanking.com/merchants/" + s.json()[j]['merchant_id'] + "?key=" + API_KEY)

                # print("lat:" + str(t.json()['geocode']['lat']) + " lng:" + str(t.json()['geocode']['lng']))

                file.write('{"type": "Feature","properties": {"mag": 5.1}, "geometry": {"type": "Point","coordinates": [' + str(t.json()["geocode"]["lng"]) + ', ' + str(t.json()["geocode"]["lat"]) + ']}},\n')

                j += 1
            i += 1
    except IndexError as e:
        pass

    file.write(']});')

    file.close()

if __name__ == "__main__":
    main()
