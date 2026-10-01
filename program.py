#Denne koden er for oppgave 3, der man skal få koden til å skrive ut en artist, alle artistene, og minst en opplysning.
import json

with open("musikkliste.json", encoding="utf-8") as fil:
    data = json.load(fil)

# print(data[0]["artistnavn"]) #(Printer kun ut det første artistnavnet i koden.)
for artist in data:
    print(artist["artistnavn"])
    print(artist["musikksjanger"])
    print(artist["gjennombrudd"])
    print(artist["land"])