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
        return country_asns
    else:
        return None

def GO_TO_ASN_NEIGHBOURS(ASN,c):
    api='https://stat.ripe.net/data/asn-neighbours/data.json?'
    url=api+ urllib.parse.urlencode({'resource':ASN})
    json_data_ASN_NEIGHBOURS = requests.get(url).json()
    liste_asn_providers=[]
    Path_Count_value=[]
    for i in json_data_ASN_NEIGHBOURS['data']['neighbours']:
        if (i['type']=='left'):
            liste_asn_providers.append(str(i['asn']))
            Path_Count_value.append(str(i['power']))
    
    print("Les Providers " +str(liste_asn_providers)+ "de valeur"+str(Path_Count_value))
    Nombre_Totale_De_Path(Path_Count_value)
    Calcul_Frequence(liste_asn_providers,c,ASN,Path_Count_value)
    #return liste_asn_providers
    #print("Les Providers de AS "+ str(ASN) + str(liste_asn_providers))

def Nombre_Totale_De_Path(liste_path):
    val=0
    for i in liste_path:
        val=val+int(i)
    #print("Le nombre Totale de Path est " +str(val))
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
                
    
    print("Les Providers Locaux du AS"+AS+" sont: "+str(Local_Providers))
    print("Les International Providers du AS"+AS+" sont: "+str(International_Providers))
    Totale=Nombre_Totale_De_Path(liste_path_count)
    print("Le Nombre Totale de Path est : "+str(Totale))
    for p in Trouver_valeur_path(International_Providers,AS):
        c=(int(p)/Totale)*100
        Frequence_Finale.append(c)
        
    #print("F= "+str(Frequence_Finale))
    DESSINER_DIAGRAMME(International_Providers,Frequence_Finale,AS)

def DESSINER_DIAGRAMME(liste,f,ASN):
    if(liste!=[]):
        plt.title("International Transit Providers of AS "+ASN+" :")
        labels=liste
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
                #print(Fre)
    #print("Les INternationales Providers "+str(Int_providers)+"avec la frequence de chacun "+str(Fre))
    return Fre
                        
                
                
                
    
    
while True:
    Country = input('Country: ')
    if (Country == 'quit' or Country =='q'):
        break
    else:
        for i in get_country_asn(Country):
            GO_TO_ASN_NEIGHBOURS(i,Country)
            #print(GO_TO_ASN_NEIGHBOURS(i,Country))
        #print("LES ASN LIBANAIS SONT : "+ str(get_country_asn(Country)))
        
        
