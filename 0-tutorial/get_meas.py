import json
from ripe.atlas.sagan import PingResult

res_file = "test_meas.json"
with open(res_file) as res_handler:
    json_results = json.load(res_handler)
    for result in json_results:
        parsed_result = PingResult.get(result)
        print(parsed_result.rtt_min)
