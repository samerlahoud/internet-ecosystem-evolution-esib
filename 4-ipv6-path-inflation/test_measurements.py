from ripe.atlas.sagan import Result
import requests
import json
import numpy
import matplotlib.pyplot as plt
from datetime import datetime

vector_ID_v6 = [12279291,12279292,12279294,12279295]
vector_ID_v4= [12279317,12279318,12279326,12279321]
result_v6=[]
result_v4=[]


for i in vector_ID_v6:
      
      result = 'https://atlas.ripe.net/api/v2/measurements/{}/results/?format=json'.format(i)
      response= requests.get(result)
      if response.status_code == 200:
         result_v6.append(json.loads(response.content.decode('utf-8')))

for i in vector_ID_v4:
      
      result = 'https://atlas.ripe.net/api/v2/measurements/{}/results/?format=json'.format(i)
      response= requests.get(result)
      if response.status_code == 200:
         result_v4.append(json.loads(response.content.decode('utf-8')))


my_result_v6 = []
my_result_v4 =[]
for i in result_v6:
     my_result_v6.append(Result.get(i[0]))
for i in result_v4:
     my_result_v4.append(Result.get(i[0]))   
total_hop_v6=[]
total_hop_v4=[]

for i in range(len(my_result_v6)):
    total_hop_v6.append(my_result_v6[i].total_hops)
for i in range(len(my_result_v4)):
    total_hop_v4.append(my_result_v4[i].total_hops)
rtt_v6=[]
rtt_v4=[]
for i in range(len(my_result_v6)):
      if my_result_v6[i].is_success:
          rtt_v6.append(my_result_v6[i].last_median_rtt)

for i in range(len(my_result_v4)):
      if my_result_v4[i].is_success:
          rtt_v4.append(my_result_v4[i].last_median_rtt)


#print(total_hop_v6)
#print(total_hop_v4)
#print(rtt_v6)
#print(rtt_v4)

diff_hopes=[]
diff_rtt=[]

for i in range(len(total_hop_v6)):
      diff_hopes.append(abs(total_hop_v6[i]-total_hop_v4[i] ))
print(diff_hopes)
for i in range(len(rtt_v6)):
      diff_rtt.append(abs(rtt_v6[i]-rtt_v4[i]))
print(diff_rtt)

bin1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
plt.hist(diff_hopes,bin1)
plt.xlabel("difference in number of hopes between v4&v6")
plt.ylabel("frequency")
plt.grid(True)
#plt.show()
date= datetime.now
filename=date().strftime('%d%m%Y%H%M%S')+".png"
plt.savefig("E:\semestre 4\ecosysteme et evolution de l'Internet\plots\Hop\{}".format(filename))

bin2=[0,10,20,30,50,100]
plt.hist(diff_rtt,bin2)
plt.xlabel("difference in value of RTT between v4&v6")
plt.ylabel("frequency")
plt.grid(True)
#plt.show()
#print(filename)
plt.savefig("E:\semestre 4\ecosysteme et evolution de l'Internet\plots\RTT\{}".format(filename))
