import urllib.request as ur
import matplotlib.pyplot as plt
import urllib.parse
import requests 
import json
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import datetime
import plotly.figure_factory as ff
import plotly.offline as offline
import os.path
from progress.bar import Bar




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
                neighbour_power = int(neighbour['power'])
                if (neighbour['type']=='left' and neighbour_asn not in country_asns):
                    if (neighbour_asn not in country_neighbours):
                        country_neighbours[neighbour_asn] = neighbour_power
                    else:
                        country_neighbours[neighbour_asn] = country_neighbours[neighbour_asn] + neighbour_power
    print(country_neighbours)
    return country_neighbours

def get_country_neighbours_Satelite(country_code, country_asns):
    country_neighbours={}
    for asn in country_asns:
        if(asn!='42020'):
            #print("studying: ", asn)
            api_url = '{}asn-neighbours/data.json?resource={}'.format(api_url_base, asn)
            asn_neighbours_json1 = requests.get(api_url)
            if (asn_neighbours_json1.status_code == 200):
                asn_neighbours_json = json.loads(asn_neighbours_json1.content.decode('utf-8'))
                for neighbour in asn_neighbours_json['data']['neighbours']:
                    neighbour_asn = str(neighbour['asn'])
                    neighbour_power = int(neighbour['power'])
                    if (neighbour['type']=='left' and neighbour_asn not in country_asns):
                        if (neighbour_asn not in country_neighbours):
                            country_neighbours[neighbour_asn] = neighbour_power
                        else:
                            country_neighbours[neighbour_asn] = country_neighbours[neighbour_asn] + neighbour_power
    #print("Les satelite providers du liban sont "+str(country_neighbours))
    return country_neighbours

def get_country_neighbours_Level3(country_code, country_asns):
    country_neighbours_division={}
    Liste_AS_libanais=[]
    Liste_AS_libanais_power=[]
    for asn in country_asns:
        print("studying: ", asn)
        api_url = '{}asn-neighbours/data.json?resource={}'.format(api_url_base, asn)
        asn_neighbours_json = requests.get(api_url).json()
        for neighbour in asn_neighbours_json['data']['neighbours']:                  #Pour  savoir a quel AS libanais Level 3 offre de l'internet 
            neighbour_asn = str(neighbour['asn'])
            neighbour_power = int(neighbour['power'])
            if (neighbour_asn=='3356'):
                Liste_AS_libanais.append(asn)
                Liste_AS_libanais_power.append(neighbour_power)
                country_neighbours_division[neighbour_asn]=Liste_AS_libanais
    print("Power: "+str(Liste_AS_libanais_power))         
    print(country_neighbours_division)
    DESSINER_DIAGRAMME_Level3(Liste_AS_libanais,Liste_AS_libanais_power,'3356')




def indexall(lst, value):
	return [i for i, v in enumerate(lst) if v == value]
       
def Remplir_liste_Pays(Dic,Country):
    Labels=[]
    Value=[]
    power_total=0
    others=0
    for cle in Dic.keys():
        Labels.append(cle)
    print(Labels)
    for cle1 in Dic.values():
        Value.append(cle1)
        power_total=power_total+cle1
    print(Value)
    Labels_Delete=[]
    Value_Delete=[]
    for clee in Value:
        if(((clee*100)/power_total) < 2.5):           #on ajoute tous les AS avec un pourcentage moins que 4% dans la categorie Others
            others=others+clee
            ind=indexall(Value,clee)
            print(ind)
            for h in ind:
                Labels_Delete.append(Labels[h])
                Value_Delete.append(Value[h])
    
    Value.append(others)
    Value=[n for n in Value if n not in Value_Delete]
    Labels=[n for n in Labels if n not in Labels_Delete]
    print()
    print("--------------")
    print(Labels)
    print("taille de Labels "+str(len(Labels)))
    print(Value)
    print("taille de Value "+str(len(Value)))
    DESSINER_DIAGRAMME(Labels,Value,Country)

def Remplir_liste_Satelite(Dic,Country):
    Labels=[]
    Value=[]
    power_total=0
    others=0
    for cle in Dic.keys():
        Labels.append(cle)
    print(Labels)
    for cle1 in Dic.values():
        Value.append(cle1)
        power_total=power_total+cle1
    print(Value)
    Labels_Delete=[]
    Value_Delete=[]
    for clee in Value:
        if(((clee*100)/power_total) < 2.5):           #on ajoute tous les AS avec un pourcentage moins que 4% dans la categorie Others
            others=others+clee
            ind=indexall(Value,clee)
            print(ind)
            for h in ind:
                Labels_Delete.append(Labels[h])
                Value_Delete.append(Value[h])
    
    Value.append(others)
    Value=[n for n in Value if n not in Value_Delete]
    Labels=[n for n in Labels if n not in Labels_Delete]
    print()
    print("--------------")
    print(Labels)
    print("taille de Labels "+str(len(Labels)))
    print(Value)
    print("taille de Value "+str(len(Value)))
    DESSINER_DIAGRAMME_Satelite(Labels,Value,Country)



def Remplir_liste_Pays2(Dic,Country,year):
    Labels=[]
    Value=[]
    power_total=0
    others=0
    for cle in Dic.keys():
        Labels.append(cle)
    for cle1 in Dic.values():
        Value.append(cle1)
        power_total=power_total+cle1
    Labels_Delete=[]
    Value_Delete=[]
    for clee in Value:
        if(((clee*100)/power_total) < 2.5):   #on ajoute tous les AS avec un pourcentage moins que 4% dans la categorie Others
            others=others+clee
            ind=indexall(Value,clee)
            for h in ind:
                Labels_Delete.append(Labels[h])
                Value_Delete.append(Value[h])
    
    Value.append(others)
    Value=[n for n in Value if n not in Value_Delete]
    Labels=[n for n in Labels if n not in Labels_Delete]
    print(Labels)
    print("taille de Labels "+str(len(Labels)))
    print(Value)
    print("taille de Value "+str(len(Value)))
    DESSINER_DIAGRAMME_Pays2(Labels,Value,Country,year)


def ASN_History2(country_code, country_asns,year):
    #URL=https://stat.ripe.net/data/asn-neighbours/data.json?resource=AS42020&starttime=2008-12-01T12:00:00
    country_neighbours={}
    for asn in country_asns:
        api_url = '{}asn-neighbours/data.json?resource={}&starttime={}-10-01T12:00:00'.format(api_url_base,asn,year)
        asn_neighbours_json1 = requests.get(api_url)
        if (asn_neighbours_json1.status_code == 200):
            asn_neighbours_json = json.loads(asn_neighbours_json1.content.decode('utf-8'))
            for neighbour in asn_neighbours_json['data']['neighbours']:
                neighbour_asn = str(neighbour['asn'])
                neighbour_power = int(neighbour['power'])
                if (neighbour['type']=='left' and neighbour_asn not in country_asns):
                    if (neighbour_asn not in country_neighbours):
                        country_neighbours[neighbour_asn] = neighbour_power
                    else:
                        country_neighbours[neighbour_asn] = country_neighbours[neighbour_asn] + neighbour_power
    print("In "+str(year)+" "+str(country_neighbours))
    return country_neighbours
    
                                                            
def Get_Year(Date):
    formatt="%Y-%m-%dT%H:%M:%S"
    dateobject = datetime.datetime.strptime(Date,formatt)
    return dateobject.year

    
    
def DESSINER_DIAGRAMME(liste,f,ASN):
    labels=[]
    sizes=[]
    x=[]
    if(liste!=[]):
        plt.title("International Transit Providers of "+ASN+" :")
        x=GET_NAME(liste)
        x.append("Others")
        print(x)
        labels=list(x)
        sizes=f
        plt.axis('equal')
        plt.pie(sizes,labels=labels,autopct='%0.1f%%')
        plt.savefig('C:/Users/abraham/Documents/GitHub/internet-ecosystem-evolution-esib/3-regional-isp/Graphs/'+ASN+'.png',bbox_inches='tight')
        plt.legend()
        plt.show()
        
        
    else:
        print("Ce AS ne possede pas de International Transit Providers")
        print()

def DESSINER_DIAGRAMME_Satelite(liste,f,ASN):
    labels=[]
    sizes=[]
    x=[]
    if(liste!=[]):
        plt.title("Internet Satelite Providers of "+ASN+" :")
        x=GET_NAME(liste)
        x.append("Others")
        print(x)
        labels=list(x)
        sizes=f
        plt.axis('equal')
        plt.pie(sizes,labels=labels,autopct='%0.1f%%')
        plt.savefig('C:/Users/abraham/Documents/GitHub/internet-ecosystem-evolution-esib/3-regional-isp/Graphs/'+ASN+'_Satelite.png',bbox_inches='tight')
        plt.legend()
        plt.show()
        
        
    else:
        print("Ce AS ne possede pas de International Transit Providers")
        print()

def DESSINER_DIAGRAMME_Level3(liste,f,ASN):
    labels=[]
    sizes=[]
    x=[]
    if(liste!=[]):
        plt.title(ASN+"'s Lebanese clients are :")
        x=GET_NAME(liste)
        labels=x
        sizes=f
        plt.axis('equal')
        plt.pie(sizes,labels=labels,autopct='%0.1f%%')
        plt.savefig('C:/Users/abraham/Documents/GitHub/internet-ecosystem-evolution-esib/3-regional-isp/Graphs/'+ASN+'.png',bbox_inches='tight')
        plt.legend()
        plt.show()
        
        
    else:
        print("Ce AS ne possede pas de International Transit Providers")
        print()

    
def DESSINER_DIAGRAMME_Pays2(liste,f,Country,year):
    labels=[]
    sizes=[]
    x=[]
    if(liste!=[]):
        plt.title("International Transit Providers of "+Country+" in " +str(year)+"  are:")
        x=GET_NAME(liste)
        x.append("Others")
        labels=x
        sizes=f
        plt.axis('equal')
        plt.pie(sizes,labels=labels,autopct='%0.1f%%')
        plt.savefig('C:/Users/abraham/Documents/GitHub/internet-ecosystem-evolution-esib/3-regional-isp/Graphs/LB/'+Country+'_'+str(year)+'.png',bbox_inches='tight')
        plt.legend()
        plt.show()

def GET_NAME(liste):
    Names=[]
    for i in liste:  
        url='https://stat.ripe.net/data/whois/data.json?resource={}'.format(i)
        json_data_AS_NAME1 = requests.get(url)
        if (json_data_AS_NAME1.status_code == 200):
            json_data_AS_NAME = json.loads(json_data_AS_NAME1.content.decode('utf-8'))
            if(i=='6453'):
                Names.append('TATA COMMUNICATIONS')
            else:
                for t in json_data_AS_NAME['data']['records']:
                    for j in t:
                        if(j['key']=='as-name' or j['key']=='ASName'):
                            Names.append(j['value'])
    return Names


def GET_NAME_One_AS(AS):
    url='https://stat.ripe.net/data/whois/data.json?resource={}'.format(AS)
    Names=[] 
    json_data_AS_NAME1 = requests.get(url)
    if (json_data_AS_NAME1.status_code == 200):
        json_data_AS_NAME = json.loads(json_data_AS_NAME1.content.decode('utf-8'))
        if(AS =='6453'):
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
            country_neighbours = get_country_neighbours(country_code, country_asns)
            Satelite=get_country_neighbours_Satelite(country_code, country_asns)
            Remplir_liste_Satelite(Satelite,country_code)
            print()
            print()
            Remplir_liste_Pays(country_neighbours,country_code)
            print("c'est Fini")
            Continuer = input("Do you want to see the International Providers of another country: ")
            if(Continuer=='yes' or Continuer=='y'):
                start()
            else:
                i=0
                year=2008
                while(i<10):
                    print("Studying year "+str(year))
                    f=ASN_History2(country_code, country_asns,year)
                    Remplir_liste_Pays2(f,country_code,year)
                    i=i+1
                    year=year+1
                    
                    
