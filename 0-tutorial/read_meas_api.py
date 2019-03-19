#Read measurement from a URL
#https://github.com/RIPE-NCC/ripe.atlas.sagan
#Documentation can be found on https://ripe-atlas-sagan.readthedocs.io/en/latest/

import requests
from ripe.atlas.sagan import PingResult

source = "https://atlas.ripe.net//api/v2/measurements/20335797/results/?format=json"
response = requests.get(source).json()

for result in response:
    parsed_result = PingResult.get(result)
    print(parsed_result.rtt_min)
