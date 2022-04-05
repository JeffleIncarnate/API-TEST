import main
import json

jsonList = []

def read_json():
    f = open("User_Data/Data.json")
    data = json.load(f)

    for i in data["test"]:
        jsonList.append(i)

    f.close()
    return jsonList

read_json()

print(jsonList)