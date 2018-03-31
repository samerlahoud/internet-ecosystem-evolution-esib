import urllib.request as ur
import matplotlib.pyplot as plt
import urllib.parse
import requests 
import json
from collections import Counter


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

    country_neighbours=[]

    for asn in country_asns:
        print("studying: ", asn)
        api_url = '{}asn-neighbours/data.json?resource={}&lod=1'.format(api_url_base, asn)
        asn_neighbours_json = requests.get(api_url).json()
        for neighbour in asn_neighbours_json['data']['neighbours']:
            neighbour_asn = str(neighbour['asn'])
            if (neighbour['type']=='left' and neighbour_asn not in country_asns and neighbour_asn not in country_neighbours):
                country_neighbours.append(neighbour_asn)
                print(neighbour_asn)
    return country_neighbours

def GO_TO_ASN_NEIGHBOURS(ASN,c):
    api='https://stat.ripe.net/data/asn-neighbours/data.json?'
    url=api+ urllib.parse.urlencode({'resource':ASN})
    json_data_ASN_NEIGHBOURS = requests.get(url).json()
    liste_asn_providers=[]
    Path_Count_value=[]
    Path_Count_value_Int=[]
    for i in json_data_ASN_NEIGHBOURS['data']['neighbours']:
        if (i['type']=='left'):
            liste_asn_providers.append(str(i['asn']))
            Path_Count_value.append(str(i['power']))
            api1='https://stat.ripe.net/data/rir/data.json?'
            url1=api1+ urllib.parse.urlencode({'resource':str(i['asn'])})+'&lod=2'
            json_data = requests.get(url1).json()
            for j in json_data['data']['rirs']:
                if (j['country']!=c):
                    Path_Count_value_Int.append(str(i['power']))
                    
                    
    print("Les Providers " +str(liste_asn_providers)+ " de valeur "+str(Path_Count_value))
    Calcul_Frequence(liste_asn_providers,c,ASN,Path_Count_value_Int)
    


def Calcul_Frequence(liste,c,AS,liste_path_count):
    Local_Providers=[]
    International_Providers=[]
    Frequence_Finale=[]
    for i in liste:
        api='https://stat.ripe.net/data/rir/data.json?'
        url=api+ urllib.parse.urlencode({'resource':i})+'&lod=2'
        json_data = requests.get(url).json()
        for j in json_data['data']['rirs']:
            if (j['country']==c):
                Local_Providers.append(i)
            else:
                International_Providers.append(i)
    print("Les International Providers du AS"+AS+" sont:"+str(International_Providers))
    for p in Trouver_valeur_path(International_Providers,AS):
        Frequence_Finale.append(int(p))
        
    DESSINER_DIAGRAMME(International_Providers,Frequence_Finale,AS)

    
    
def Calculer_Frequence_Pays(liste_asn,Int_liste):
    for i in liste_asn:
        for j in Int_liste:
            Trouver_valeur_path(j,i)
    print(Trouver_valeur_path(j,i))

def Trouver_International_Providers_Au_Liban(Country):
    liste_asn_providers=[]
    International_Providers=[]
    Country_ASN=get_country_asn(Country)
    for i in Country_ASN:
        api='https://stat.ripe.net/data/asn-neighbours/data.json?'
        url=api+ urllib.parse.urlencode({'resource':i})
        json_data_ASN_NEIGHBOURS = requests.get(url).json()
        for j in json_data_ASN_NEIGHBOURS['data']['neighbours']:
            if (j['type']=='left'):
                liste_asn_providers.append(str(j['asn']))
    a=set(liste_asn_providers)
    b=list(a)
    print(b)
    for p in b:
        api='https://stat.ripe.net/data/rir/data.json?'
        url=api+ urllib.parse.urlencode({'resource':p})+'&lod=2'
        json_data = requests.get(url).json()
        for t in json_data['data']['rirs']:
            if (t['country']!=Country):
                International_Providers.append(p)
    x=set(International_Providers)
    y=list(x)
    print("Les International Providers du Liban sont:"+str(y))
    return y

#------------------------------------------------------------------------------------------------------------------------------------------


def Trouver_Frequence_International_Providers_Liban(Liste_Internationa_Providers_Liban,ASN,Internationa_Provider_AS,Value_AS_Path):
    Liste=[]
    Val=0
    for i in Liste_Internationa_Providers_Liban:
        for j in ASN:
            for p in Internationa_Provider_AS:
                if(i==p):
                    #Val=Val+Value_AS_Path[Internationa_Provider_AS.index(p)]
                    Liste.append(Value_AS_Path[Internationa_Provider_AS.index(p)])
    print(Liste)

#---------------------------------------------------------------------------------------------------------------------------------------------
    
    
    

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
        plt.show()
        
    else:
        print("Ce AS ne possede pas de International Transit Providers")
        print()

def DESSINER_DIAGRAMME_Pays(liste,f,Country):
    labels=[]
    sizes=[]
    if(liste!=[]):
        plt.title("International Transit Providers of "+ Country+ " are")
        labels=GET_NAME(liste)
        sizes=f
        plt.pie(sizes,autopct='%1.1f%%')
        plt.legend(labels,bbox_to_anchor=(0.85,1), loc=2, borderaxespad=0.)
        plt.axis('equal')
        plt.show()


                                    
def Trouver_valeur_path(Int_providers,AS):
    api='https://stat.ripe.net/data/asn-neighbours/data.json?'
    url=api+ urllib.parse.urlencode({'resource':AS})
    json_data_ASN_NEIGHBOURS = requests.get(url).json()
    Fre=[]
    for i in json_data_ASN_NEIGHBOURS['data']['neighbours']:
        for j in Int_providers:
            if (i['asn']==int(j)):
                Fre.append(str(i['power']))
    return Fre




def Trouver_valeur_path_Pays(Int_providers,Liste_AS):
    Fre=[]
    for i in Int_providers:
        val=0
        for j in Liste_AS:
            api='https://stat.ripe.net/data/asn-neighbours/data.json?'
            url=api+ urllib.parse.urlencode({'resource':j})
            json_data_ASN_NEIGHBOURS = requests.get(url).json()
            neigh_list = json_data_ASN_NEIGHBOURS['data']['neighbours']
            for p in neigh_list:
                if(i==str(p['asn'])):
                    val=val+p['power']
                    Fre.insert(Int_providers.index(i),str(val))
            print("La  valeur de "+str(i)+" est de" +str(Fre)+" pour le provider "+str(j))
    del Fre[len(Int_providers):]
    return Fre




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

def GET_NAME1(liste):
    #url=https://stat.ripe.net/data/as-overview/data.json?resource=AS42020
    api ='https://stat.ripe.net/data/as-overview/data.json?'
    Names=[]
    for i in liste:  
        url=api+ urllib.parse.urlencode({'resource':i})
        json_data_AS_NAME = requests.get(url).json()
        for t in json_data_AS_NAME['data']['holder']:
            Names.append(t)
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
        
    
                
                              

while True:
    country_code = input('Country two-letter code: ')
    if (country_code == 'quit' or country_code =='q'):
        break
    else:
        country_asns = get_country_asn(country_code)
        print(country_asns)
        country_neighbours = get_country_neighbours(country_code, country_asns)
        print(country_neighbours)
        
        #o=Trouver_International_Providers_Au_Liban(Country)
        #a=Trouver_valeur_path_Pays(o,c)
        #DESSINER_DIAGRAMME_Pays(o,a,Country)
        #Trouver_Frequence_International_Providers_Liban(o,c,International_Providers,Frequence_Finale)
        #for i in get_country_asn(Country):
        #    GO_TO_ASN_NEIGHBOURS(i,Country)
        
        
