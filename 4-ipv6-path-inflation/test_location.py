#j=requests.get('http://ip-api.com/json/130.206.216.2')
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

idv6=[12459070,12459079,12459088,12599687,12599693,12599699,12599711]
idv4=[12459144,12459154,12459163,12599748,12599755,12599761,12599793]
#AS-PATH de IR:
#idv6=[12459071,12459080,12459089,12599688,12599694,12599700,12599712]
#idv4=[12459145,12459155,12459164,12599749,12599756,12599762,12599794]
result= requests.get('https://atlas.ripe.net/api/v2/measurements/{}/results/?&format=json'.format(idv6[3]))
response=json.loads(result.content.decode('utf-8'))
my_result = Result.get(response[5])
hop= my_result.hops
ip=[]
for k in hop:
    packet= k.packets
    for j in packet:
        if (j.origin not in ip) and (j.origin != 'None'):
            ip.append(j.origin)
    #print(ip)

path=[]
for k in ip:
    j=requests.get("http://ip-api.com/json/{}".format(k))
    if j.status_code == 200:
        r=json.loads(j.content.decode('utf-8'))
        if r['status']=='success':
            path.append(r['country'])
        else:
            path.append(0)
print(path)
