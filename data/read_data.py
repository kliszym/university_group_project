import json

with open("ap1_A.txt", "r") as ap1, open("ap2_A.txt", "r") as ap2, open("ap3_A.txt", 'r') as ap3:
    ap1_data = json.load(ap1)
    ap2_data = json.load(ap2)
    ap3_data = json.load(ap3)

data = zip(ap1_data, ap2_data, ap3_data)
for line in data:
    print(line)
    break
