from datetime import datetime
from ripe.atlas.cousteau import (
  Ping,
  Traceroute,
  AtlasSource,
  AtlasCreateRequest
)

ATLAS_API_KEY = "c378f9e4-6a66-4847-a228-46949edf64bf"

ping = Ping(af=4, target="speedtest.omantel.om", description="LB and BH to OA")

traceroute = Traceroute(
    af=4,
    target="speedtest.omantel.om",
    description="testing",
    protocol="ICMP",
)

source1 = AtlasSource(
    type="country",
    value="LB",
    requested=3,
    tags={"include":["system-ipv4-works"]}
)

source2 = AtlasSource(
    type="country",
    value="BH",
    requested=3,
    tags={"include":["system-ipv4-works"]}
)

atlas_request = AtlasCreateRequest(
    start_time=datetime.utcnow(),
    key=ATLAS_API_KEY,
    measurements=[ping, traceroute],
    sources=[source1, source2],
    is_oneoff=True
)

(is_success, response) = atlas_request.create()
