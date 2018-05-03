
from ripe.atlas.cousteau import AtlasStopRequest

ATLAS_STOP_API_KEY = "ce8c8d26-dc88-4fa6-9923-34b8ac3207c2"

vector_ID_v6 = []
f = open("C:/Users/Florian Mouchantaf/Desktop/ipv6.txt",'r')

for line in f:
    vector_ID_v6.append(int(line.strip()))
    
vector_ID_v4= []
f = open("C:/Users/Florian Mouchantaf/Desktop/ipv4.txt",'r')

for line in f:
    vector_ID_v4.append(int(line.strip()))


for i in vector_ID_v6:
    atlas_request = AtlasStopRequest(msm_id=i, key=ATLAS_STOP_API_KEY)

    (is_success, response) = atlas_request.create()

for i in vector_ID_v4:
    atlas_request = AtlasStopRequest(msm_id=i, key=ATLAS_STOP_API_KEY)
    (is_success, response) = atlas_request.create()
  
