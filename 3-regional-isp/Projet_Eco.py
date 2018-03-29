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
        print("LES AS : " + str(country_asns))
        print()
        return country_asns
    else:
        return None

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

def Nombre_Totale_De_Path(liste_Int):
    val=0
    for i in liste_Int:
        val=val+int(i)
    return val
        


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
    #print("Les Providers Locaux du AS"+AS+" sont: "+str(Local_Providers))
    print("Les International Providers du AS"+AS+" sont:"+str(International_Providers))
    
    #Totale=Nombre_Totale_De_Path(liste_path_count)
    #print("Le Nombre Totale de Path est : "+str(Totale))
    
    for p in Trouver_valeur_path(International_Providers,AS):
        Frequence_Finale.append(int(p))
            
    DESSINER_DIAGRAMME(International_Providers,Frequence_Finale,AS)

    
    
def Calculer_Frequence_Pays(liste_asn,Int_liste):
    for i in liste_asn:
        for j in Int_liste:
            Trouver_valeur_path(j,i)
    print(Trouver_valeur_path(j,i))
            
        
    
    


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

def DESSINER_DIAGRAMME_Pays(liste,f,c):
    labels=[]
    sizes=[]
    if(liste!=[]):
        plt.title("International Transit Providers of "+c+" :")
        labels=GET_NAME(liste)
        sizes=f
        plt.pie(sizes,labels=labels,autopct='%1.1f%%')
        #argument explode qui permet de mettre en valeur une des part du diagramme
        plt.show()
    else:
        print("Ce AS ne possede pas de International Transit Providers")
        print()
        
        

                
                
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


def GET_NAME(liste):
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
        
    
                
                              

while True:
    Country = input('Country: ')
    if (Country == 'quit' or Country =='q'):
        break
    else:
        for i in get_country_asn(Country):
            GO_TO_ASN_NEIGHBOURS(i,Country)
        
        
