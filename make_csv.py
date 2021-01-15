import json
import os

from ap_ids import get_ap_id

data_directory = "data"
result_file = data_directory + "/data.csv"

data_files = os.listdir("data")
print(data_files)

with open(result_file, "w") as f_result:
    csv_header = "AP_id;Point_id;RSSI;Time;"
    f_result.write(csv_header + '\n')
    for data_file in data_files:
        if data_file[-4:] == ".txt":
            with open(data_directory + "/" + data_file) as f_data:
                data = json.load(f_data)
                for value in data:
                    csv_line = get_ap_id(value["BSSID"]) + ';' + value["Area"] + ';' + str(value["RSSI"]) + ';' + value["Time"] + ';'
                    f_result.write(csv_line + '\n')
                    print(csv_line)
