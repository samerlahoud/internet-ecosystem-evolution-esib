from datetime import datetime, timedelta
from ripe.atlas.cousteau import (
  Ping,
  Traceroute,
  AtlasSource,
  AtlasCreateRequest
)

ATLAS_API_KEY = "c378f9e4-6a66-4847-a228-46949edf64bf"

ping = Ping(af=4, target="speedtest.omantel.om", description="ping BH to OA")

traceroute = Traceroute(
    af=4,
    target="speedtest.omantel.om",
    description="traceroute BH to OA",
    protocol="ICMP",
)

source = AtlasSource(
    type="country",
    value="BH",
    requested=3,
    tags={"include":["system-ipv4-works"]}
)

atlas_request = AtlasCreateRequest(
    start_time=datetime.utcnow()+timedelta(seconds=60),
    key=ATLAS_API_KEY,
    measurements=[ping, traceroute],
    sources=[source],
    is_oneoff=True
)

(is_success, response) = atlas_request.create()

print(response)
print(is_success)
