import json

jsonList = []

def read_json():
    # Better With Statement
    with open("User_Data/Data.json") as f:
        lines = json.load(f)

        for i in lines["test"]:
            jsonList.append(i)

        return jsonList