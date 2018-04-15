from datetime import datetime
import urllib.request as ur
import urllib.parse
import requests 
import json
from ripe.atlas.cousteau import AtlasResultsRequest
from ripe.atlas.cousteau import (Ping,Traceroute,AtlasSource,AtlasCreateRequest)
from ripe.atlas.cousteau import AtlasStopRequest
import time


#url=https://atlas.ripe.net/api/v2/measurements/12156409/
#url=https://atlas.ripe.net/api/v2/measurements/12156409/results/?format=json

ATLAS_API_KEY = "7e69aca2-f7a3-4119-8ccb-dd7f1edebd11"

ping = Ping(af=4, target="google.com.lb", description="testing new wrapper")

source1 = AtlasSource(type="asn", value= 6453, requested=1)
#source2 = AtlasSource(type="asn", value= 174, requested=1)
#source3 = AtlasSource(type="asn", value= 3356, requested=1)
sourcess=[source1]

atlas_request = AtlasCreateRequest(
    key=ATLAS_API_KEY,
    measurements=[ping],
    sources=sourcess,
    is_oneoff=True
)

(is_success, response) = atlas_request.create()
print(atlas_request.create())
msm_id=atlas_request.create()[1]
meas=msm_id['measurements']
res=meas[0]
print(res)



api_url_base = 'https://atlas.ripe.net/api/v2/'
api_url = 'https://atlas.ripe.net/api/v2/measurements/{}/results/?format=json'.format(res)
time.sleep(300)
response = requests.get(api_url).json()
print(type(response))
for i in response:
    print("Le RTT de "+str(sources[response.index(i)].value)+" est "+str(i['avg']))


