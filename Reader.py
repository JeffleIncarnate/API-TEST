import json

def read_json():
    # Better With Statement
    with open("User_Data/Data.json") as f:
        lines = json.load(f)

    return lines["test"]