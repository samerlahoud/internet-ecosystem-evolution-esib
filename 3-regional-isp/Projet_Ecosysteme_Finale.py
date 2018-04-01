import urllib.request as ur
import matplotlib.pyplot as plt
import urllib.parse
import requests 
import json
from collections import Counter
from collections import defaultdict
import plotly.plotly as py
import plotly.graph_objs as go
import plotly

plotly.tools.set_credentials_file(username='pierre12', api_key='EF5vrYMDIXU36y0vTxNb')
plotly.tools.set_config_file(plotly_domain='https://plot.ly',plotly_streaming_domain='stream.plot.ly')

#url=https://stat.ripe.net/data/asn-neighbours/data.json?resource=AS42020

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
        api_url = '{}asn-neighbours/data.json?resource={}&lod=1'.format(api_url_base, asn)
        asn_neighbours_json = requests.get(api_url).json()
        for neighbour in asn_neighbours_json['data']['neighbours']:
            neighbour_asn = str(neighbour['asn'])
            neighbour_power = int(neighbour['power'])
            if (neighbour['type']=='left' and neighbour_asn not in country_asns):
                if (neighbour_asn not in country_neighbours):
                    country_neighbours[neighbour_asn] = neighbour_power
                else:
                    country_neighbours[neighbour_asn] = country_neighbours[neighbour_asn] + neighbour_power
    return country_neighbours

def get_neighbours_AS(AS,country_asns):
    AS_neighbours={}
    Liste=[]
    Neighbours=[]
    api_url = '{}asn-neighbours/data.json?resource={}&lod=1'.format(api_url_base,AS)
    asn_neighbours_json = requests.get(api_url).json()
    for neighbour in asn_neighbours_json['data']['neighbours']:
        neighbour_asn = str(neighbour['asn'])
        neighbour_power = int(neighbour['power'])
        if (neighbour['type']=='left' and neighbour_asn not in country_asns):
            Neighbours.append(neighbour_asn)
            Liste.append(neighbour_power)
    #print("INT:"+str(Neighbours)+"Valwue:"+str(Liste))
    AS_neighbours[AS]=Liste
    #print("LOLLLLL"+str(AS_neighbours))
    DESSINER_DIAGRAMME(Neighbours,Liste,AS)
    
            
        
def Remplir_liste_Pays(Dic,Country):
    Labels=[]
    Value=[]
    for cle in Dic.keys():
        Labels.append(cle)
    for cle1 in Dic.values():
        Value.append(cle1)
    print(Labels)
    print(Value)
    DESSINER_DIAGRAMME_Pays(Labels,Value,Country)
        
    

def DESSINER_DIAGRAMME(liste,f,ASN):
    labels=[]
    sizes=[]
    if(liste!=[]):
        plt.title("International Transit Providers of "+str(GET_NAME_One_AS(ASN))+" :")
        labels=GET_NAME(liste)
        sizes=f
        plt.pie(sizes,autopct='%1.1f%%')
        plt.legend(labels,bbox_to_anchor=(0.85,1), loc=2, borderaxespad=0.)
        plt.axis('equal')
        plt.tight_layout()
        plt.show()
        
    else:
        print("Ce AS ne possede pas de International Transit Providers")
        print()

def DESSINER_DIAGRAMME_Pays(liste,f,Country):
    fig = {
        'data': [{'labels': GET_NAME(liste),
                  'values':f,
                  'type': 'pie'}],
        'layout': {'title': 'International Transit Providers of '+Country+ 'are'}
         }

    py.plot(fig)


def GET_NAME(liste):
    #url=https://stat.ripe.net/data/as-overview/data.json?resource=AS42020
    api ='https://stat.ripe.net/data/whois/data.json?'
    Names=[]
    for i in liste:  
        url=api+ urllib.parse.urlencode({'resource':i})
        json_data_AS_NAME = requests.get(url).json()
        if(i=='6453'):
            Names.append('TATA COMMUNICATIONS')
        else:
            for t in json_data_AS_NAME['data']['records']:
                for j in t:
                    if(j['key']=='as-name' or j['key']=='ASName'):
                        Names.append(j['value'])
    return Names

def GET_NAME_One_AS(AS):
    api ='https://stat.ripe.net/data/whois/data.json?'
    Names=[] 
    url=api+ urllib.parse.urlencode({'resource':i})
    json_data_AS_NAME = requests.get(url).json()
    if(AS=='6453'):
        Names.append('TATA COMMUNICATIONS')
    else:
        for t in json_data_AS_NAME['data']['records']:
            for j in t:
                if(j['key']=='as-name' or j['key']=='ASName'):
                    Names.append(j['value'])
    return Names

def start():     
    while True:
        country_code = input('Country two-letter code: ')
        if (country_code == 'quit' or country_code =='q'):
            break
        else:
            country_asns = get_country_asn(country_code)
            #print(country_asns)
            country_neighbours = get_country_neighbours(country_code, country_asns)
            #print(country_neighbours)
            Remplir_liste_Pays(country_neighbours,country_code)
            Continuer = input("Do you want to see the International Providers of another country: ")
            if(Continuer=='yes' or Continuer=='y'):
                start()
            else:
                for i in get_country_asn(country_code):
                    get_neighbours_AS(i,country_asns)
                
