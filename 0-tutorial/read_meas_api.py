import requests
from ripe.atlas.sagan import PingResult

source = "https://atlas.ripe.net//api/v2/measurements/20335797/results/?format=json"
response = requests.get(source).json()

for result in response:
    parsed_result = PingResult.get(result)
    print(parsed_result.rtt_min)
