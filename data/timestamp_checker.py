ap_times = {
    "AP1": {
        "A": [],
        "B": [],
        "C": [],
        "D": [],
        "E": [],
        "F": [],
        "G": [],
        "H": [],
        "I": [],
        "J": [],
        "K": [],
        "L": [],
        "TEST-DL": [],
        "TEST-GH": [],
        "TEST-K": []
    },
    "AP2": {
        "A": [],
        "B": [],
        "C": [],
        "D": [],
        "E": [],
        "F": [],
        "G": [],
        "H": [],
        "I": [],
        "J": [],
        "K": [],
        "L": [],
        "TEST-DL": [],
        "TEST-GH": [],
        "TEST-K": []
    },
    "AP3": {
        "A": [],
        "B": [],
        "C": [],
        "D": [],
        "E": [],
        "F": [],
        "G": [],
        "H": [],
        "I": [],
        "J": [],
        "K": [],
        "L": [],
        "TEST-DL": [],
        "TEST-GH": [],
        "TEST-K": []
    },
    "AP4": {
        "A": [],
        "B": [],
        "C": [],
        "D": [],
        "E": [],
        "F": [],
        "G": [],
        "H": [],
        "I": [],
        "J": [],
        "K": [],
        "L": [],
        "TEST-DL": [],
        "TEST-GH": [],
        "TEST-K": []
    }
}


def check_unique_time(ap_id, area, time):
    if time in ap_times[ap_id][area]:
        return False
    else:
        ap_times[ap_id][area].append(time)
        return True
