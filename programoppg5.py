import json
import random

with open("vitser.json", encoding="utf-8") as fil:
    data = json.load(fil)

#print(data["jokes"][0]["joke"]) #printer den første vitsen.

#for vits in data["jokes"]:
    #print(vits["joke"])     #Printer alle vitsene. 
#print("Antall vitser:", len(data["jokes"])) #Printer antall vitser. 

sokeord = input("Skriv inn et ord du vil søke etter: ")

for vits in data["jokes"]:
    if sokeord.lower() in vits["joke"].lower():
        print(vits["joke"])

#tilfeldig_vits = random.choice(data["jokes"])
#print(tilfeldig_vits["joke"])                 #Tilfeldig vits. 