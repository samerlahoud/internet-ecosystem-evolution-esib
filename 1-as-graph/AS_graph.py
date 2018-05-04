import json
import requests

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
    providers={}
    clients={}
    for asn in country_asns:
        api_url = '{}asn-neighbours/data.json?resource={}&lod=1'.format(api_url_base, asn)
        asn_neighbours_json = requests.get(api_url).json()
        for neighbour in asn_neighbours_json['data']['neighbours']:
            neighbour_asn = str(neighbour['asn'])
            neighbour_power = int(neighbour['power'])
            if (neighbour['type']=='left' and neighbour_asn not in country_asns):
                if (neighbour_asn not in providers):
                    providers[neighbour_asn] = neighbour_power
                else:
                    providers[neighbour_asn] = providers[neighbour_asn] + neighbour_power

            if (neighbour['type']=='right' and neighbour_asn not in country_asns):
                if (neighbour_asn not in clients):
                    clients[neighbour_asn] = neighbour_power
                else:
                    clients[neighbour_asn] = clients[neighbour_asn] + neighbour_power
    return (providers, clients)


def get_local_or_international_AS(AS,country_asns):
    AS_neighbours={}
    Liste_local=[]
    Liste_international=[]
    Liste=[]
    local_neighbours=[]
    international_neighbours=[]
    api_url = '{}asn-neighbours/data.json?resource={}&lod=1'.format(api_url_base,AS)
    asn_neighbours_json = requests.get(api_url).json()
    for neighbour in asn_neighbours_json['data']['neighbours']:
        neighbour_asn = str(neighbour['asn'])
        neighbour_power = int(neighbour['power'])
        if (neighbour['type']=='left' and neighbour_asn not in country_asns):
            international_neighbours.append(neighbour_asn)
            Liste_international.append(neighbour_power)
        if (neighbour_asn in country_asns):
            local_neighbours.append(neighbour_asn)
            Liste_local.append(neighbour_power)
    Liste = Liste_international + Liste_local
    AS_neighbours[AS]=Liste

