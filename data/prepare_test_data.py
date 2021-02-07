import json
import os

from ap_ids import APs, get_ap_id
from timestamp_checker import check_unique_time

data_directory = "raw_tests"
result_directory = "APs_tests"

for key, value in APs.items():
    open(result_directory + "/" + key, "w").close()

data_files = os.listdir(data_directory)
print(data_files)

for data_file in data_files:
    with open(data_directory + "/" + data_file) as f_data:
        data = json.load(f_data)
        APs = result_directory + "/" + get_ap_id(data[0]["BSSID"])
        with open(APs, "a") as f_result:
            for value in data:
                if not check_unique_time(get_ap_id(value["BSSID"]), value["Area"], value["Time"]):
                    continue
                json_data = json.dumps({
                    "Area": value["Area"],
                    "RSSI": str(value["RSSI"]),
                    "Time": value["Time"]
                })
                f_result.write(json_data + '\n')
                print(json_data)
