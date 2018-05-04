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

def get_ISP_LB(country_asns):
    Liste={}
    #https://stat.ripe.net/data/asn-neighbours/data.json?resource=AS9051
    for asn in country_asns:
        if(asn!="42020"):
            api_url = '{}asn-neighbours/data.json?resource={}'.format(api_url_base, asn)
            asn_neighbours_json = requests.get(api_url).json()
            for neighbour in asn_neighbours_json['data']['neighbours']:
                neighbour_asn = str(neighbour['asn'])
                if (neighbour['type']=='left' and neighbour_asn not in country_asns):
                    Liste[asn]=neighbour_asn
    print(Liste)
    Transforme_Dic_Liste(Liste)
    
def Transforme_Dic_Liste(dic):
    Cle=[]
    Value=[]
    for i in dic.keys():
        Cle.append(i)
    for j in dic.values():
        Value.append(j)
    x=get_country_neighbours('LB', Cle)
    print(x)
    

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
    AS_neighbours[AS]=Liste
    DESSINER_DIAGRAMME(Neighbours,Liste,AS)

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
        if(((clee*100)/power_total) < 4):           #on ajoute tous les AS avec un pourcentage moins que 4% dans la categorie Others
            others=others+clee
            ind=indexall(Value,clee)
            print(ind)
            for h in ind:
                Labels_Delete.append(Labels[h])
                Value_Delete.append(Value[h])
    print(list(set(Labels_Delete)))
    print(list(set(Value_Delete)))

       
    Value.append(others)
    Value=[n for n in Value if n not in Value_Delete]
    Labels=[n for n in Labels if n not in Labels_Delete]
    print()
    print("--------------")
    print(Labels)
    print(Value)
    
    
    DESSINER_DIAGRAMME(Labels,Value,Country)

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
        if(((clee*100)/power_total) < 4):   #on ajoute tous les AS avec un pourcentage moins que 4% dans la categorie Others
            others=others+clee
            ind=indexall(Value,clee)
            for h in ind:
                Labels_Delete.append(Labels[h])
                Value_Delete.append(Value[h])
    print(list(set(Labels_Delete)))
    print(list(set(Value_Delete)))

        
    Value.append(others)
    Value=[n for n in Value if n not in Value_Delete]
    Labels=[n for n in Labels if n not in Labels_Delete]

    DESSINER_DIAGRAMME_Pays2(Labels,Value,Country,year)


def ASN_History2(country_code, country_asns,year):
    #URL=https://stat.ripe.net/data/asn-neighbours/data.json?resource=AS42020&starttime=2008-12-01T12:00:00
    country_neighbours={}
    for asn in country_asns:
        api_url = '{}asn-neighbours/data.json?resource={}&starttime={}-10-01T12:00:00'.format(api_url_base,asn,year)
        asn_neighbours_json = requests.get(api_url).json()
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
        x.append('Others')
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
        x.append('Others')
        labels=x
        sizes=f
        plt.axis('equal')
        plt.pie(sizes,labels=labels,autopct='%0.1f%%')
        plt.savefig('C:/Users/abraham/Documents/GitHub/internet-ecosystem-evolution-esib/3-regional-isp/Graphs/LB/'+Country+'_'+str(year)+'.png',bbox_inches='tight')
        plt.legend()
        plt.show()

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
    url=api+ urllib.parse.urlencode({'resource':AS})
    json_data_AS_NAME = requests.get(url).json()
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
            #get_ISP_LB(country_asns)
            print()
            print()
            print("hehe"+str(country_neighbours))
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
                    
                    
