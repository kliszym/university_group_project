ap_times = {
    "AP1": {
        "A": [],
        "B": [],
        "C": [],
        "D": [],
        "E": []
    },
    "AP2": {
        "A": [],
        "B": [],
        "C": [],
        "D": [],
        "E": []
    },
    "AP3": {
        "A": [],
        "B": [],
        "C": [],
        "D": [],
        "E": []
    },
    "AP4": {
        "A": [],
        "B": [],
        "C": [],
        "D": [],
        "E": []
    }
}


def check_unique_time(ap_id, area, time):
    if time in ap_times[ap_id][area]:
        return False
    else:
        ap_times[ap_id][area].append(time)
        return True
