from ripe.atlas.cousteau import ProbeRequest
from datetime import datetime
from ripe.atlas.cousteau import (
  Ping,
  AtlasCreateRequest,
  AtlasSource
)
from ripe.atlas.cousteau import AtlasResultsRequest
ATLAS_API_KEY = "7c41f68b-8b75-4e00-848a-df272e255da8"
ping = Ping(af=6, target="www.google.com", description="testing ping")

source1 = AtlasSource(
    type="country",
    value="LB",
    requested=50,
   tags={"include":["system-ipv6-works"] }
)
#atlas_request = AtlasCreateRequest(
    #start_time=datetime.utcnow(),
 #   key=ATLAS_API_KEY,
  #  measurements=[ping],
   # sources=[source1],
    #is_oneoff=True
#)
#(is_success, response) = atlas_request.create()
#print (response)
kwargs = {"msm_id":11998012}
is_success, results = AtlasResultsRequest(**kwargs).create()

if is_success:
    print(results)
#filters = {"country_code": "LB" ,"tags": "system-ipv6-works" }
#probes = ProbeRequest(**filters)


#for probe in probes:
 #   print(probe["asn_v6"])

 #Print total count of found probes
#print(probes.total_count)
