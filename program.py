import json

with open("musikkliste.json", encoding="utf-8") as fil:
    data = json.load(fil)

print(data[0]["artistnavn"])