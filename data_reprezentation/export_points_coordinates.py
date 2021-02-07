import json

from data.retrieve_distance import distance

with open("points.json", "w") as f:
    result = json.dump(distance, f, indent=2)
