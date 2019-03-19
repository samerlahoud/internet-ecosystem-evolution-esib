#Read measurement from a local file
#https://github.com/RIPE-NCC/ripe.atlas.sagan
#Documentation can be found on https://ripe-atlas-sagan.readthedocs.io/en/latest/

import json
from ripe.atlas.sagan import PingResult

res_file = "result_sample.json"
with open(res_file) as res_handler:
    json_results = json.load(res_handler)
    for result in json_results:
        parsed_result = PingResult.get(result)
        print(parsed_result.rtt_min)
