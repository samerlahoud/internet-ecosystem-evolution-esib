from ripe.atlas.cousteau import ProbeRequest
from datetime import datetime
from ripe.atlas.cousteau import (
 Traceroute,
  AtlasCreateRequest,
  AtlasSource
)
from ripe.atlas.cousteau import AtlasResultsRequest
import requests
ATLAS_API_KEY = "df5d3613-6c53-43be-bdad-cb921ffd20cf"
traceroute16 = Traceroute(af=4, target="fr-bod-as198985.anchors.atlas.ripe.net", interval=36000,description="traceroute v4 to France", protocol="ICMP")
source_LB_1 = AtlasSource(
    type="asn",
    value="9051",
    requested=1,
   tags={"include":["system-ipv6-works"]}
)
atlas_request = AtlasCreateRequest(
            #start_time=datetime.utcnow(),
            key=ATLAS_API_KEY,
            measurements=[traceroute16],
            sources=[source_LB_1],
            is_oneoff=False,
            start_time=1525348200,
            stop_time=1525693800
        )
(is_success, response) = atlas_request.create()
print(is_success)
print(response)
msm_id =response['measurements'][0]
print(msm_id)
