import json

with open("prelim_application_response20250320 1.json", "r", encoding="utf-8") as f:
    data = json.load(f)

data = data['data']



for i in data:
    try:
        iterator = iter(data[i])
        print("Length of each Key : " , i, ": " , len(data[i]))
    except:
        continue


