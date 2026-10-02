import json
import random

with open("vitser.json", encoding="utf-8") as fil:
    data = json.load(fil)

while True:    

# Menyen
 print("1. Vis første vits")
 print("2. Vis alle vitser")
 print("3. Tell antall vitser")
 print("4. Søk etter ord")
 print("5. Vis tilfeldig vits")
 print("6. Avslutt")

 valg = input("Velg 1-6: ") #Brukeren kan skrive hvilken som den ønsker


 if valg == "1":
     print(data["jokes"][0]["joke"])  # Printer den første vitsen i vitselista.


 elif valg == "2":
     for vits in data["jokes"]:
         print(vits["joke"])  # Printer alle vitsene som er i vitselista.


 elif valg == "3":
     print("Antall vitser:", len(data["jokes"]))  # Printer antall vitser som er i vitselista.


 elif valg == "4":
     sokeord = input("Skriv inn et ord du vil søke etter: ") #Brukeren kan skrive ulike bokstaver eller ord (f.eks "it"), og få opp alle vitsene som inneholder den teksten.

     for vits in data["jokes"]:
         if sokeord.lower() in vits["joke"].lower():
             print(vits["joke"])  # Input der brukeren kan søke etter ord selv. 


 elif valg == "5":
     tilfeldig_vits = random.choice(data["jokes"])
     print(tilfeldig_vits["joke"])  # Printer en tilfeldig vits.

 elif valg == "6":
    print("Programmet avsluttes.")  
    break                           #Avslutter programmet med funksjonen break.

# Deler av denne koden har jeg fått hjelp av ChatGPT til å lage. 