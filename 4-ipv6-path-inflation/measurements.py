from ripe.atlas.sagan import Result
import requests
import json
result="https://atlas.ripe.net/api/v2/measurements/11847770/results/"

response = requests.get(result)
if response.status_code == 200:
      test = json.loads(response.content.decode('utf-8'))
      print(test[0])

my_result = Result.get(test[5])

print(my_result.af)
# Returns 6

print(my_result.last_median_rtt)
# Returns 123.456 
