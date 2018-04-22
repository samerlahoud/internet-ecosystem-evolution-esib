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
traceroute1 = Traceroute(af=6, target="jp-tyo-as2500.anchors.atlas.ripe.net", description="traceroute  to Japan", protocol="ICMP")
traceroute2 = Traceroute(af=6, target="za-cpt-as37663.anchors.atlas.ripe.net", description="traceroute  to South Africa", protocol="ICMP")
traceroute3 = Traceroute(af=6, target="fr-bod-as198985.anchors.atlas.ripe.net", description="traceroute to France Bordeaux", protocol="ICMP")
traceroute4 = Traceroute(af=6, target="kw-kwi-as42961.anchors.atlas.ripe.net", description="traceroute to Kuwait", protocol="ICMP")
traceroute5 = Traceroute(af=4, target="jp-tyo-as2500.anchors.atlas.ripe.net", description="traceroute v4 to Japan", protocol="ICMP")
traceroute6 = Traceroute(af=4, target="za-cpt-as37663.anchors.atlas.ripe.net", description="traceroute v4 to South Africa", protocol="ICMP")
traceroute7 = Traceroute(af=4, target="fr-bod-as198985.anchors.atlas.ripe.net", description="traceroute v4 to France Bordeaux", protocol="ICMP")
traceroute8 = Traceroute(af=4, target="kw-kwi-as42961.anchors.atlas.ripe.net", description="traceroute v4 to Kuwait", protocol="ICMP")

source_LB = AtlasSource(
    type="asn",
    value="41833",
    requested=1,
   tags={"include":["system-ipv6-works"]}
)
source_IR = AtlasSource(
    type="asn",
    value="6736",
    requested=1,
   tags={"include":["system-ipv6-works"]}
)
source_TR = AtlasSource(
    type="asn",
    value="25145",
    requested=1,
   tags={"include":["system-ipv6-works"]}
)
source_OM = AtlasSource(
    type="asn",
    value="206350",
    requested=1,
   tags={"include":["system-ipv6-works"]}
)



atlas_request = AtlasCreateRequest(
   # start_time=datetime.utcnow(),
    key=ATLAS_API_KEY,
    measurements=[traceroute3],
    sources=[source_LB],
    is_oneoff=True
)
(is_success, response) = atlas_request.create()
#print (response)
msm_id =response['measurements']
print (msm_id)





















#kwargs = {"msm_id":12222554}
#is_success, results = AtlasResultsRequest(**kwargs).create()

#if is_success:
 #   print(results)
#filters = {"country_code": "LB" ,"tags": "system-ipv6-works" }
#probes = ProbeRequest(**filters)


#for probe in probes:
 #   print(probe["asn_v6"])

 #Print total count of found probes
#print(probes.total_count)
