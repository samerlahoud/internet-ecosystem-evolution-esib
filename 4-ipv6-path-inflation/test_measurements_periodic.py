from ripe.atlas.sagan import Result
import requests
import json
import numpy
import matplotlib.pyplot as plt
from datetime import datetime
from statistics import mean
import matplotlib.ticker as mticker

vector_ID_v6 = []
f = open("C:/Users/Florian Mouchantaf/Desktop/ipv6.txt",'r')

for line in f:
    vector_ID_v6.append(int(line.strip()))
f.close()

f = open("C:/Users/Florian Mouchantaf/Desktop/ipv6_1.txt",'r')

for line in f:
    vector_ID_v6.append(int(line.strip()))
f.close()

vector_ID_v4= []
f = open("C:/Users/Florian Mouchantaf/Desktop/ipv4.txt",'r')

for line in f:
    vector_ID_v4.append(int(line.strip()))
f.close()

f = open("C:/Users/Florian Mouchantaf/Desktop/ipv4_1.txt",'r')

for line in f:
    vector_ID_v4.append(int(line.strip()))
f.close()


result_v6=[]
result_v4=[]
total_hop_v6=[]
total_hop_v4=[]
rtt_v6=[]
rtt_v4=[]

def average_hope(list):
    hop_avg=[]
    for k in list :
        if (Result.get(k).is_success):
            hop_avg.append(Result.get(k).total_hops)
    if (len(hop_avg)==0):
        hop_avg.append(0)
    return mean(hop_avg)
def average_rtt(list):
    rtt_avg=[]
    for k in list :
        if (Result.get(k).is_success):
            rtt_avg.append(Result.get(k).last_median_rtt)
    if (len(rtt_avg)==0):
        rtt_avg.append(0)
    return mean(rtt_avg)


for i,j in zip(vector_ID_v6,vector_ID_v4):
      
      resultv6 = 'https://atlas.ripe.net/api/v2/measurements/{}/results/?format=json'.format(i)
      responsev6= requests.get(resultv6)
      resultv4 = 'https://atlas.ripe.net/api/v2/measurements/{}/results/?format=json'.format(j)
      responsev4= requests.get(resultv4)
      if responsev6.status_code == 200:
         result_v6=json.loads(responsev6.content.decode('utf-8'))
         
      if responsev4.status_code == 200:
         result_v4=json.loads(responsev4.content.decode('utf-8'))
      hopv6=average_hope(result_v6)
      hopv4=average_hope(result_v4)
      if  (hopv6 != 0) and (hopv4 !=0) :
          total_hop_v6.append(hopv6)
          total_hop_v4.append(hopv4)
      rttv6=average_rtt(result_v6)
      rttv4=average_rtt(result_v4)
      if (rttv6 !=0) and (rttv4 !=0):
          rtt_v4.append(rttv4)
          rtt_v6.append(rttv6)

diff_hopes=[]
diff_rtt=[]

#print(total_hop_v6)
#print(total_hop_v4)
      
for i in range(len(total_hop_v6)):
      diff_hopes.append(total_hop_v6[i]-total_hop_v4[i] )

for i in range(len(rtt_v6)):
      diff_rtt.append(rtt_v6[i]-rtt_v4[i])
      
#mesures reussis:
      
print(len(diff_hopes))
print (len(diff_rtt))
date= datetime.now
filename=date().strftime('%d%m%Y%H%M%S')+".png"


#(bin1=[-20,-10,-5,-3,0,3,5,10,20])
bin1=numpy.linspace(-15,15,31)
plt.hist(diff_hopes,bin1, edgecolor='black', linewidth=1.3)
plt.xlabel("difference in number of hopes between v4&v6")
plt.ylabel("percentage")
plt.grid(True)
formatter = mticker.PercentFormatter(xmax=45)
plt.gca().yaxis.set_major_formatter(formatter)
#plt.show()
plt.savefig("E:\semestre 4\ecosysteme et evolution de l'Internet\plots\Hop\{}".format(filename))

bin2=[-150,-50,-40,-30,-20,-10,-5,0,5,10,20,30,40,50,150]
#bin2=numpy.linspace(-50,50,11)
#plt.hist(diff_rtt,bin2,edgecolor='black',linewidth=1)
plt.xlabel("difference in value of RTT between v4&v6")
plt.ylabel("percentage")
#plt.xscale('symlog',basex=2)
plt.grid(True)
formatter = mticker.PercentFormatter(xmax=45)
plt.gca().yaxis.set_major_formatter(formatter)
#plt.show()
#print(filename)
#plt.savefig("E:\semestre 4\ecosysteme et evolution de l'Internet\plots\RTT\{}".format(filename))





