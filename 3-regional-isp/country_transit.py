import urllib.request as ur
import matplotlib.pyplot as plt
import urllib.parse
import requests 
import json
import datetime
import sys
import os.path

api_url_base = 'https://stat.ripe.net/data/'


def get_country_asn(country_code):
    api_url = '{}country-asns/data.json?resource={}&lod=1'.format(api_url_base, country_code)

    response = requests.get(api_url)
    
    if response.status_code == 200:
        country_asns_json = json.loads(response.content.decode('utf-8'))
        country_asns = country_asns_json["data"]["countries"][0]["routed"]
        return country_asns
    else:
        return None

def get_country_neighbours(country_code, country_asns):
    country_neighbours={}
    for asn in country_asns:
        #print("studying: ", asn)
        api_url = '{}asn-neighbours/data.json?resource={}'.format(api_url_base, asn)
        asn_neighbours_json1 = requests.get(api_url)
        if (asn_neighbours_json1.status_code == 200):
            asn_neighbours_json = json.loads(asn_neighbours_json1.content.decode('utf-8'))
            for neighbour in asn_neighbours_json['data']['neighbours']:
                neighbour_asn = str(neighbour['asn'])
                neighbour_v4_peers = int(neighbour['v4_peers'])
                if (neighbour['type']=='left' and neighbour_asn not in country_asns):
                    if (neighbour_asn not in country_neighbours):
                        country_neighbours[neighbour_asn] = neighbour_v4_peers
                    else:
                        country_neighbours[neighbour_asn] = country_neighbours[neighbour_asn] + neighbour_v4_peers
    print(country_neighbours)
    return country_neighbours

if __name__ == "__main__":    
    with open('countries.json', 'r') as f:
        countries = json.load(f)
    global_country_neighbours = dict();
    for country_code in countries.values():
        country_asns = get_country_asn(country_code)
        country_neighbours = get_country_neighbours(country_code, country_asns)
        global_country_neighbours[country_code] = country_neighbours
    print(global_country_neighbours)
    with open('inter_transit.json', 'w') as fp:
        json.dump(global_country_neighbours, fp)
