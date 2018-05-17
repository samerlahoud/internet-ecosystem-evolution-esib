from ripe.atlas.sagan import Result
import requests
import json
import pyasn
asndb = pyasn.pyasn('C:/Users/Florian Mouchantaf/AppData/Local/Programs/Python/Python36-32/Scripts/ipasn_db_20180512.1600.dat')

x=asndb.lookup('8.8.8.8')
#print(x[0])
#ftp://archive.routeviews.org//bgpdata/2018.05/RIBS/rib.20180512.1600.bz2

#pyasn_util_convert.py --single rib.20180512.1600.bz2 ipasn_db_20180512.1600.dat


#public api:
#https://api.iptoasn.com/v1/as/ip/<ip address>

#AS-path de la source LB2(IDM):
aspath=[]
path=[]
idv6=[12459070,12459079,12459088,12599687,12599693,12599699,12599711]
idv4=[12459144,12459154,12459163,12599748,12599755,12599761,12599793]
#AS-PATH de IR:
#idv6=[12459071,12459080,12459089,12599688,12599694,12599700,12599712]
#idv4=[12459145,12459155,12459164,12599749,12599756,12599762,12599794]
for i in idv4:
    result= requests.get('https://atlas.ripe.net/api/v2/measurements/{}/results/?&format=json'.format(i))
    response=json.loads(result.content.decode('utf-8'))
    my_result = Result.get(response[0])
    hop= my_result.hops
    ip=[]
    for k in hop:
        packet= k.packets
        for j in packet:
            if (j.origin not in ip) and (j.origin != 'None'):
                ip.append(j.origin)
        #print(ip)

    AS=[]

    for k in ip:
        j=requests.get("https://api.iptoasn.com/v1/as/ip/{}".format(k))
        if j.status_code == 200:
            r=json.loads(j.content.decode('utf-8'))
            #print(r)
            if r['announced']:
                l=r['as_number']
                if l not in AS:
                    AS.append(l)
                    #description.append(r['as_description'])
    description=[]
    for i in AS:
        
        j=requests.get("https://stat.ripe.net/data/as-overview/data.json?resource=AS{}".format(i))
        if j.status_code == 200:
                r=json.loads(j.content.decode('utf-8'))
        description.append(r['data']['holder'])
    print(description)


#print(country)
    
