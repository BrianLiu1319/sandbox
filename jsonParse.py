import json

with open("Business Account Opening_DictionaryFile.json", "r", encoding="utf-8") as f:
    data = json.load(f)


print(type(data['pages'][0]["inputs"]))

lst = []

for j in range(len(data['pages'])):
    for i in range(len(data['pages'][j]["inputs"])):
        lst.append({"id":data['pages'][j]["inputs"][i]['id'],
        "type":data['pages'][j]["inputs"][i]['type'],
        "label":data['pages'][j]["inputs"][i]['label']})


