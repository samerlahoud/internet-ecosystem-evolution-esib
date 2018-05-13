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


result= requests.get('https://atlas.ripe.net/api/v2/measurements/12459073/results/?&format=json')
response=json.loads(result.content.decode('utf-8'))
my_result = Result.get(response[7])
hop= my_result.hops

ip=[]
for i in hop:
    packet= i.packets
    for j in packet:
        if (j.origin not in ip) and (j.origin != 'None'):
            ip.append(j.origin)
#print(ip)

AS=[]
for i in ip:
    j=requests.get("https://api.iptoasn.com/v1/as/ip/{}".format(i))
    if j.status_code == 200:
         r=json.loads(j.content.decode('utf-8'))
         if r['as_number'] not in AS:
             AS.append(r['as_number'])

    
print (AS)
