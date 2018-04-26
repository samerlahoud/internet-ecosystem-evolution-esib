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
traceroute5 = Traceroute(af=6, target="uy-mvd-as28000.anchors.atlas.ripe.net", description="traceroute to Uruguay", protocol="ICMP")
traceroute6 = Traceroute(af=6, target="ca-mtr-as852.anchors.atlas.ripe.net", description="traceroute to Montreal", protocol="ICMP")
traceroute7 = Traceroute(af=6, target="in-bom-as33480.anchors.atlas.ripe.net", description="traceroute to Inde", protocol="ICMP")
traceroute8 = Traceroute(af=6, target="es-leg-as766.anchors.atlas.ripe.net", description="traceroute to Spain", protocol="ICMP")

traceroute9 = Traceroute(af=4, target="jp-tyo-as2500.anchors.atlas.ripe.net", description="traceroute v4 to Japan", protocol="ICMP")
traceroute10 = Traceroute(af=4, target="za-cpt-as37663.anchors.atlas.ripe.net", description="traceroute v4 to South Africa", protocol="ICMP")
traceroute11 = Traceroute(af=4, target="fr-bod-as198985.anchors.atlas.ripe.net", description="traceroute v4 to France Bordeaux", protocol="ICMP")
traceroute12 = Traceroute(af=4, target="kw-kwi-as42961.anchors.atlas.ripe.net", description="traceroute v4 to Kuwait", protocol="ICMP")
traceroute13 = Traceroute(af=4, target="uy-mvd-as28000.anchors.atlas.ripe.net", description="traceroute v4 to Uruguay", protocol="ICMP")
traceroute14 = Traceroute(af=4, target="ca-mtr-as852.anchors.atlas.ripe.net", description="traceroute v4 to Montreal", protocol="ICMP")
traceroute15 = Traceroute(af=4, target="in-bom-as33480.anchors.atlas.ripe.net", description="traceroute v4 to Inde", protocol="ICMP")
traceroute16 = Traceroute(af=4, target="es-leg-as766.anchors.atlas.ripe.net", description="traceroute v4 to Spain", protocol="ICMP")

source_LB_1 = AtlasSource(
    type="asn",
    value="41833",
    requested=1,
   tags={"include":["system-ipv6-works"]}
)
source_LB_2 = AtlasSource(
    type="asn",
    value="9051",
    requested=1,
   tags={"include":["system-ipv6-works"]}
)
source_LB_3 = AtlasSource(
    type="asn",
    value="203615",
    requested=1,
   tags={"include":["system-ipv6-works"]}
)
source_IR_1 = AtlasSource(
    type="asn",
    value="6736",
    requested=1,
   tags={"include":["system-ipv6-works"]}
)
source_IR_2 = AtlasSource(
    type="asn",
    value="50530",
    requested=1,
   tags={"include":["system-ipv6-works"]}
)
source_IR_3 = AtlasSource(
    type="asn",
    value="43754",
    requested=1,
   tags={"include":["system-ipv6-works"]}
)
source_TR_1 = AtlasSource(
    type="asn",
    value="25145",
    requested=1,
   tags={"include":["system-ipv6-works"]}
)
source_TR_2 = AtlasSource(
    type="asn",
    value="199159",
    requested=1,
   tags={"include":["system-ipv6-works"]}
)
source_TR_3 = AtlasSource(
    type="asn",
    value="42910",
    requested=1,
   tags={"include":["system-ipv6-works"]}
)
source_OM = AtlasSource(
    type="asn",
    value="206350",
    requested=1,
   tags={"include":["system-ipv6-works"]}
)
source_QA = AtlasSource(
    type="asn",
    value="8781",
    requested=1,
   tags={"include":["system-ipv6-works"]}
)
source_IQ = AtlasSource(
    type="asn",
    value="44217",
    requested=1,
   tags={"include":["system-ipv6-works"]}
)


vector_ID_v6=[]
vector_ID_v4=[]





#IPV6 measurements:
atlas_request = AtlasCreateRequest(
   # start_time=datetime.utcnow(),
    key=ATLAS_API_KEY,
    measurements=[traceroute1],
    sources=[source_LB_1,source_LB_2,source_LB_3,source_IR_1,source_IR_2,source_IR_3,source_TR_1,source_TR_2,source_TR_3,source_OM,source_QA,source_IQ],
    is_oneoff=True
)
(is_success, response) = atlas_request.create()
#print (response)
msm_id =response['measurements']
vector_ID_v6.append(msm_id)


atlas_request = AtlasCreateRequest(
   # start_time=datetime.utcnow(),
    key=ATLAS_API_KEY,
    measurements=[traceroute2],
    sources=[source_LB_1,source_LB_2,source_LB_3,source_IR_1,source_IR_2,source_IR_3,source_TR_1,source_TR_2,source_TR_3,source_OM,source_QA,source_IQ],
    is_oneoff=True
)
(is_success, response) = atlas_request.create()
#print (response)
msm_id =response['measurements']
vector_ID_v6.append(msm_id)

atlas_request = AtlasCreateRequest(
   # start_time=datetime.utcnow(),
    key=ATLAS_API_KEY,
    measurements=[traceroute3],
    sources=[source_LB_1,source_LB_2,source_LB_3,source_IR_1,source_IR_2,source_IR_3,source_TR_1,source_TR_2,source_TR_3,source_OM,source_QA,source_IQ],
    is_oneoff=True
)
(is_success, response) = atlas_request.create()
#print (response)
msm_id =response['measurements']
vector_ID_v6.append(msm_id)

atlas_request = AtlasCreateRequest(
   # start_time=datetime.utcnow(),
    key=ATLAS_API_KEY,
    measurements=[traceroute4],
    sources=[source_LB_1,source_LB_2,source_LB_3,source_IR_1,source_IR_2,source_IR_3,source_TR_1,source_TR_2,source_TR_3,source_OM,source_QA,source_IQ],
    is_oneoff=True
)
(is_success, response) = atlas_request.create()
#print (response)
msm_id =response['measurements']
vector_ID_v6.append(msm_id)


atlas_request = AtlasCreateRequest(
   # start_time=datetime.utcnow(),
    key=ATLAS_API_KEY,
    measurements=[traceroute5],
    sources=[source_LB_1,source_LB_2,source_LB_3,source_IR_1,source_IR_2,source_IR_3,source_TR_1,source_TR_2,source_TR_3,source_OM,source_QA,source_IQ],
    is_oneoff=True
)
(is_success, response) = atlas_request.create()
#print (response)
msm_id =response['measurements']
vector_ID_v6.append(msm_id)


atlas_request = AtlasCreateRequest(
   # start_time=datetime.utcnow(),
    key=ATLAS_API_KEY,
    measurements=[traceroute6],
    sources=[source_LB_1,source_LB_2,source_LB_3,source_IR_1,source_IR_2,source_IR_3,source_TR_1,source_TR_2,source_TR_3,source_OM,source_QA,source_IQ],
    is_oneoff=True
)
(is_success, response) = atlas_request.create()
#print (response)
msm_id =response['measurements']
vector_ID_v6.append(msm_id)


atlas_request = AtlasCreateRequest(
   # start_time=datetime.utcnow(),
    key=ATLAS_API_KEY,
    measurements=[traceroute7],
    sources=[source_LB_1,source_LB_2,source_LB_3,source_IR_1,source_IR_2,source_IR_3,source_TR_1,source_TR_2,source_TR_3,source_OM,source_QA,source_IQ],
    is_oneoff=True
)
(is_success, response) = atlas_request.create()
#print (response)
msm_id =response['measurements']
vector_ID_v6.append(msm_id)

atlas_request = AtlasCreateRequest(
   # start_time=datetime.utcnow(),
    key=ATLAS_API_KEY,
    measurements=[traceroute8],
    sources=[source_LB_1,source_LB_2,source_LB_3,source_IR_1,source_IR_2,source_IR_3,source_TR_1,source_TR_2,source_TR_3,source_OM,source_QA,source_IQ],
    is_oneoff=True
)
(is_success, response) = atlas_request.create()
#print (response)
msm_id =response['measurements']
vector_ID_v6.append(msm_id)



# ipv4 measurements:

atlas_request = AtlasCreateRequest(
   # start_time=datetime.utcnow(),
    key=ATLAS_API_KEY,
    measurements=[traceroute9],
    sources=[source_LB_1,source_LB_2,source_LB_3,source_IR_1,source_IR_2,source_IR_3,source_TR_1,source_TR_2,source_TR_3,source_OM,source_QA,source_IQ],
    is_oneoff=True
)
(is_success, response) = atlas_request.create()
#print (response)
msm_id =response['measurements']
vector_ID_v4.append(msm_id)

atlas_request = AtlasCreateRequest(
   # start_time=datetime.utcnow(),
    key=ATLAS_API_KEY,
    measurements=[traceroute10],
    sources=[source_LB_1,source_LB_2,source_LB_3,source_IR_1,source_IR_2,source_IR_3,source_TR_1,source_TR_2,source_TR_3,source_OM,source_QA,source_IQ],
    is_oneoff=True
)
(is_success, response) = atlas_request.create()
#print (response)
msm_id =response['measurements']
vector_ID_v4.append(msm_id)



atlas_request = AtlasCreateRequest(
   # start_time=datetime.utcnow(),
    key=ATLAS_API_KEY,
    measurements=[traceroute11],
    sources=[source_LB_1,source_LB_2,source_LB_3,source_IR_1,source_IR_2,source_IR_3,source_TR_1,source_TR_2,source_TR_3,source_OM,source_QA,source_IQ],
    is_oneoff=True
)
(is_success, response) = atlas_request.create()
#print (response)
msm_id =response['measurements']
vector_ID_v4.append(msm_id)



atlas_request = AtlasCreateRequest(
   # start_time=datetime.utcnow(),
    key=ATLAS_API_KEY,
    measurements=[traceroute12],
    sources=[source_LB_1,source_LB_2,source_LB_3,source_IR_1,source_IR_2,source_IR_3,source_TR_1,source_TR_2,source_TR_3,source_OM,source_QA,source_IQ],
    is_oneoff=True
)
(is_success, response) = atlas_request.create()
#print (response)
msm_id =response['measurements']
vector_ID_v4.append(msm_id)

atlas_request = AtlasCreateRequest(
   # start_time=datetime.utcnow(),
    key=ATLAS_API_KEY,
    measurements=[traceroute13],
    sources=[source_LB_1,source_LB_2,source_LB_3,source_IR_1,source_IR_2,source_IR_3,source_TR_1,source_TR_2,source_TR_3,source_OM,source_QA,source_IQ],
    is_oneoff=True
)
(is_success, response) = atlas_request.create()
#print (response)
msm_id =response['measurements']
vector_ID_v4.append(msm_id)

atlas_request = AtlasCreateRequest(
   # start_time=datetime.utcnow(),
    key=ATLAS_API_KEY,
    measurements=[traceroute14],
    sources=[source_LB_1,source_LB_2,source_LB_3,source_IR_1,source_IR_2,source_IR_3,source_TR_1,source_TR_2,source_TR_3,source_OM,source_QA,source_IQ],
    is_oneoff=True
)
(is_success, response) = atlas_request.create()
#print (response)
msm_id =response['measurements']
vector_ID_v4.append(msm_id)

atlas_request = AtlasCreateRequest(
   # start_time=datetime.utcnow(),
    key=ATLAS_API_KEY,
    measurements=[traceroute15],
    sources=[source_LB_1,source_LB_2,source_LB_3,source_IR_1,source_IR_2,source_IR_3,source_TR_1,source_TR_2,source_TR_3,source_OM,source_QA,source_IQ],
    is_oneoff=True
)
(is_success, response) = atlas_request.create()
#print (response)
msm_id =response['measurements']
vector_ID_v4.append(msm_id)


atlas_request = AtlasCreateRequest(
   # start_time=datetime.utcnow(),
    key=ATLAS_API_KEY,
    measurements=[traceroute16],
    sources=[source_LB_1,source_LB_2,source_LB_3,source_IR_1,source_IR_2,source_IR_3,source_TR_1,source_TR_2,source_TR_3,source_OM,source_QA,source_IQ],
    is_oneoff=True
)
(is_success, response) = atlas_request.create()
#print (response)
msm_id =response['measurements']
vector_ID_v4.append(msm_id)
