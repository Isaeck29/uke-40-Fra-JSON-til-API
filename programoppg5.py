import json

with open("vitser.json", encoding="utf-8") as fil:
    data = json.load(fil)

#print(data["jokes"][0]["joke"]) #printer den første vitsen.

#for vits in data["jokes"]:
    #print(vits["joke"])     #Printer alle vitsene. 