APs = {
    "AP1": "64:D1:54:95:E4:FD",
    "AP2": "64:D1:54:95:E8:06",
    "AP3": "CC:2D:E0:03:0F:53",
    "AP4": None
}


def get_ap_id(value_looked_for):
    for key, value in APs.items():
        if value == value_looked_for:
            return key