import requests

URL = 'http://stash.compjour.org/samples/cpsc/recalls201604.json'

def get_data():
    resp = requests.get(URL)
    return resp.json()
