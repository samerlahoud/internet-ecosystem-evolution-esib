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
traceroute16 = Traceroute(af=4, target="es-leg-as766.anchors.atlas.ripe.net", description="traceroute v4 to Spain", protocol="ICMP")
source_LB_1 = AtlasSource(
    type="asn",
    value="41833",
    requested=1,
   tags={"include":["system-ipv6-works"]}
)
atlas_request = AtlasCreateRequest(
            #start_time=datetime.utcnow(),
            key=ATLAS_API_KEY,
            measurements=[traceroute16],
            sources=[source_LB_1],
            is_oneoff=False,
            interval=180,
            start_time=1524909867,
            stop_time=1524910867
        )
(is_success, response) = atlas_request.create()
print(is_success)
print(response)
msm_id =response['measurements'][0]
print(msm_id)
