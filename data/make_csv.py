import json

from retrieve_distance import get_distance

data_directory = "APs"
result_file = "result/data.csv"
validation_file = "result/validation.csv"

with open(result_file, "w") as f_result:
    with open(validation_file, "w") as f_validation:
        csv_header = "Point_id,RSSI_AP1,RSSI_AP2,RSSI_AP3,Time,distance_x,distance_y"
        f_result.write(csv_header + '\n')

        with open(data_directory + "/" + "AP1") as f_data1:
            with open(data_directory + "/" + "AP2") as f_data2:
                with open(data_directory + "/" + "AP3") as f_data3:
                    iterator = 0
                    while(True):
                        try:
                            data1 = json.loads(f_data1.readline())
                            data2 = json.loads(f_data2.readline())
                            data3 = json.loads(f_data3.readline())
                            csv_line = data1["Area"] + ',' + \
                                       str(data1["RSSI"]) + ',' + \
                                       str(data2["RSSI"]) + ',' + \
                                       str(data3["RSSI"]) + ',' + \
                                       data1["Time"] + ',' + \
                                       str(get_distance(data1["Area"])["y"]) + ',' +\
                                       str(get_distance(data1["Area"])["x"])

                            if iterator % 20 == 0:
                                f_validation.write(csv_line + '\n')
                            else:
                                f_result.write(csv_line + '\n')

                            print(csv_line)
                            iterator += 1
                        except:
                            break
