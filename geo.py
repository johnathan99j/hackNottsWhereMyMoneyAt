#!/usr/bin/python
import requests
import sys
from scipy.interpolate import interp1d

from envVariables import API_KEY


def main():
    i, j = 0, 0

    # cust id -> account(s) id -> purchase(s) id -> merchant id -> gps
    # custId = "59f45071a73e4942cdafe49f" # Non Local
    # custId = "59f45070a73e4942cdafe49e" # Local

    if len(sys.argv) != 2:
        exit("Error: Must pass customer id as first and only arguemnt")

    custId = sys.argv[1]

    file = open("capital_one_open_bank/static/GeoJSONP.js", "w")

    file.write('eqfeed_callback({"type": "FeatureCollection","features": [')

    r = requests.get("http://api.reimaginebanking.com/customers/" + custId + "/accounts?key=" + API_KEY)

    try:
        # Loop though all the customers accounts
        while r.json()[i]['_id'] != "":
            s = requests.get("http://api.reimaginebanking.com/accounts/" + str(r.json()[i]['_id']) + "/purchases?key=" + API_KEY)

            # Loop though all the purchases in this account
            while s.json()[j]['merchant_id'] != "":
                t = requests.get("http://api.reimaginebanking.com/merchants/" + str(s.json()[j]['merchant_id']) + "?key=" + API_KEY)
                file.write('{"type": "Feature","properties": {"mag": ' + str(calcMag(s.json()[j]["amount"])) + '}, "geometry": {"type": "Point","coordinates": [' + str(t.json()["geocode"]["lng"]) + ', ' + str(t.json()["geocode"]["lat"]) + ']}},\n')

                j += 1
            i += 1
    except IndexError:
        pass

    file.write(']});')

    file.close()


def calcMag(money):

    if money > 512:
        money = 511
    elif money < 0:
        money = 0

    m = interp1d([0, 512], [3, 6])

    return m(money)
    pass


if __name__ == "__main__":
    main()
