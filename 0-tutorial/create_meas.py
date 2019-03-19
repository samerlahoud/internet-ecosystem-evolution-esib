#Create a measurement using Cousteau library
#Documentation can be found on https://github.com/RIPE-NCC/ripe-atlas-cousteau
#Cousteau tries to comply with https://atlas.ripe.net/docs/api/v2/manual/measurements/types/

from datetime import datetime, timedelta
from ripe.atlas.cousteau import (
  Ping,
  Traceroute,
  AtlasSource,
  AtlasCreateRequest
)

#Use your API Key https://atlas.ripe.net/docs/keys/
ATLAS_API_KEY = " "

#IPv4 ping and traceroute towards speedtest server in Oman
ping = Ping(af=4, target="speedtest.omantel.om", description="ping BH to OA")

traceroute = Traceroute(
    af=4,
    target="speedtest.omantel.om",
    description="traceroute BH to OA",
    protocol="ICMP",
)

#Source of measurement is a set of 3 probes in Bahrain
source = AtlasSource(
    type="country",
    value="BH",
    requested=3,
    tags={"include":["system-ipv4-works"]}
)

#Create the measurement
atlas_request = AtlasCreateRequest(
    start_time=datetime.utcnow()+timedelta(seconds=60),
    key=ATLAS_API_KEY,
    measurements=[ping, traceroute],
    sources=[source],
    is_oneoff=True
)

(is_success, response) = atlas_request.create()

#Print measurement IDs
print(response)
print(is_success)
