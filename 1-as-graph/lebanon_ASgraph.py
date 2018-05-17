import json
import requestsimport json
import requests
import networkx as nx
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
import csv

output_file='./AS_file.txt'

api_url_base = 'https://stat.ripe.net/data/'

G=nx.DiGraph()

categories={}


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
    i=0
    dct={}
    for asn in country_asns:
        G.add_node(asn)
        print(asn)
        providers={}
        clients={}
        international_neighbours=[]
        local_neighbours1=[]
        local_neighbours2=[]
        local_neighbours=[]
        api_url = '{}asn-neighbours/data.json?resource={}&lod=1'.format(api_url_base, asn)
        asn_neighbours_json = requests.get(api_url).json()
        for neighbour in asn_neighbours_json['data']['neighbours']:
            neighbour_asn = str(neighbour['asn'])
            neighbour_power = int(neighbour['power'])
            if (neighbour['type']=='left'):
                if (neighbour_asn not in providers):
                    providers[neighbour_asn] = neighbour_power
                else:
                    providers[neighbour_asn] = providers[neighbour_asn] + neighbour_power
                G.add_edge(neighbour_asn,asn,weight=neighbour_power)
                
                if(neighbour_asn not in country_asns):
                    international_neighbours.append(neighbour_asn)
                    G.node[neighbour_asn]['geo']=1 #1 for international
                else:
                    local_neighbours1.append(neighbour_asn)
                    G.node[neighbour_asn]['geo']=0 #0 for local


            if (neighbour['type']=='right'):
                local_neighbours2.append(neighbour_asn)
                if (neighbour_asn not in clients):
                    clients[neighbour_asn] = neighbour_power
                else:
                    clients[neighbour_asn] = clients[neighbour_asn] + neighbour_power
                G.add_edge(asn,neighbour_asn,weight=neighbour_power)
                G.node[neighbour_asn]['geo']=0 #0 for local
                    #for n in G.nodes():
                    #G.node[n]['artist']=G.node[n]['cat']
            
            local_neighbours=local_neighbours1+local_neighbours2
    
        G.node[asn]['cat']=categories[asn]
        
        for n in G.nodes():
            G.node[n]['name']= n
            G.node[n]['playcount']=G.degree(n)


        if (providers == dct):
            print("No providers")
        else:
            print("Providers: " , providers)
        if (clients == dct):
            print("No Clients")
        else:
            print("Clients: " , clients)
        print("International: " , international_neighbours)
        print("Local: " , local_neighbours)
            
    nx.draw(G,with_labels=True)
    plt.show()
    plt.close()



if __name__=="__main__":
    with open(output_file,'r') as csvfile:
        secteur = csv.reader(csvfile, delimiter=',')
        for row in secteur:
            categories[row[0]]=row[1]
    cc="LB"
    country_asn=get_country_asn(cc)
#country_asn=['42020','9051','41833']
    get_country_neighbours(cc,country_asn)


    G.nodes(data=True)

    data = json_graph.node_link_data(G)
    with open('graph.json', 'w') as f:
        json.dump(data, f, indent=4)



