from ripe.atlas.cousteau import ProbeRequest
from datetime import datetime
from ripe.atlas.cousteau import (
 Traceroute,
  AtlasCreateRequest,
  AtlasSource
)
from ripe.atlas.cousteau import AtlasResultsRequest
import requests
import time
ATLAS_API_KEY = "df5d3613-6c53-43be-bdad-cb921ffd20cf"
traceroute1 = Traceroute(af=6, target="jp-tyo-as2500.anchors.atlas.ripe.net", description="traceroute  to Japan",interval=10800, protocol="ICMP")
traceroute2 = Traceroute(af=6, target="za-cpt-as37663.anchors.atlas.ripe.net", description="traceroute  to South Africa",interval=10800, protocol="ICMP")
traceroute3 = Traceroute(af=6, target="fr-bod-as198985.anchors.atlas.ripe.net", description="traceroute to France Bordeaux", interval=10800, protocol="ICMP")
traceroute4 = Traceroute(af=6, target="kw-kwi-as42961.anchors.atlas.ripe.net", description="traceroute to Kuwait", interval=10800, protocol="ICMP")
traceroute5 = Traceroute(af=6, target="uy-mvd-as28000.anchors.atlas.ripe.net", description="traceroute to Uruguay",interval=10800, protocol="ICMP")
traceroute6 = Traceroute(af=6, target="ca-mtr-as852.anchors.atlas.ripe.net", description="traceroute to Montreal",interval=10800, protocol="ICMP")
traceroute7 = Traceroute(af=6, target="in-bom-as33480.anchors.atlas.ripe.net", description="traceroute to Inde",interval=10800, protocol="ICMP")
traceroute8 = Traceroute(af=6, target="es-leg-as766.anchors.atlas.ripe.net", description="traceroute to Spain",interval=10800, protocol="ICMP")

traceroute9 = Traceroute(af=4, target="jp-tyo-as2500.anchors.atlas.ripe.net", description="traceroute v4 to Japan",interval=10800, protocol="ICMP")
traceroute10 = Traceroute(af=4, target="za-cpt-as37663.anchors.atlas.ripe.net", description="traceroute v4 to South Africa",interval=10800, protocol="ICMP")
traceroute11 = Traceroute(af=4, target="fr-bod-as198985.anchors.atlas.ripe.net", description="traceroute v4 to France Bordeaux",interval=10800, protocol="ICMP")
traceroute12 = Traceroute(af=4, target="kw-kwi-as42961.anchors.atlas.ripe.net", description="traceroute v4 to Kuwait",interval=10800, protocol="ICMP")
traceroute13 = Traceroute(af=4, target="uy-mvd-as28000.anchors.atlas.ripe.net", description="traceroute v4 to Uruguay",interval=10800, protocol="ICMP")
traceroute14 = Traceroute(af=4, target="ca-mtr-as852.anchors.atlas.ripe.net", description="traceroute v4 to Montreal",interval=10800, protocol="ICMP")
traceroute15 = Traceroute(af=4, target="in-bom-as33480.anchors.atlas.ripe.net", description="traceroute v4 to Inde",interval=10800, protocol="ICMP")
traceroute16 = Traceroute(af=4, target="es-leg-as766.anchors.atlas.ripe.net", description="traceroute v4 to Spain",interval=10800, protocol="ICMP")

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


measurement_v6=[]
measurement_v6.append(traceroute1)
measurement_v6.append(traceroute2)
measurement_v6.append(traceroute3)
measurement_v6.append(traceroute4)
measurement_v6.append(traceroute5)
measurement_v6.append(traceroute6)
measurement_v6.append(traceroute7)
measurement_v6.append(traceroute8)

measurement_v4=[]
measurement_v4.append(traceroute9)
measurement_v4.append(traceroute10)
measurement_v4.append(traceroute11)
measurement_v4.append(traceroute12)
measurement_v4.append(traceroute13)
measurement_v4.append(traceroute14)
measurement_v4.append(traceroute15)
measurement_v4.append(traceroute16)
#Probes sources:
probes=[]
probes.append(source_LB_1)
probes.append(source_LB_2)
#probes.append(source_LB_3)
probes.append(source_IR_1)
#probes.append(source_IR_2)
probes.append(source_IR_3)
probes.append(source_TR_1)
probes.append(source_TR_2)
probes.append(source_TR_3)
probes.append(source_OM)
probes.append(source_QA)
#probes.append(source_IQ)
#print (sources)
file = open("C:/Users/Florian Mouchantaf/Desktop/ipv6.txt",'w')
for j in measurement_v6:
    for i in probes:
        atlas_request = AtlasCreateRequest(
            #start_time=datetime.utcnow(),
            key=ATLAS_API_KEY,
            measurements=[j],
            sources=[i],
            is_oneoff=False,
            start_time=1525366800,
            stop_time=1527865200
        )
        (is_success, response) = atlas_request.create()
        #print(is_success)
        msm_id =response['measurements'][0]
        #print(msm_id)
        file.write(str(msm_id)+"\n") 
file.close()
time.sleep(200)

file = open("C:/Users/Florian Mouchantaf/Desktop/ipv4.txt",'w')
for j in measurement_v4:
    for i in probes:
        atlas_request = AtlasCreateRequest(
            #start_time=datetime.utcnow(),
            key=ATLAS_API_KEY,
            measurements=[j],
            sources=[i],
            is_oneoff=False,
            start_time=1525366800,
            stop_time=1527865200
        )
        (is_success, response) = atlas_request.create()
        msm_id =response['measurements'][0]
        #print(msm_id)
        file.write(str(msm_id)+"\n")
    time.sleep(30)
file.close()


