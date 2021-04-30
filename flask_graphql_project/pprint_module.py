# pprint is module in python it is used to convert python data structures into well defined formatted and more readable way.
import requests
from pprint import pprint

def gecode(address):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=AIzaSyBz6e1jPcP6su0AXwljHaxcM225NUftH9U"
    resp = requests.get(url, params = {'address': address})
    return resp.json()


data = gecode('India gate')
pprint(data)