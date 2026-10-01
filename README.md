# Hva har jeg gjort i denne oppgaven?

* ## Jeg har laget en musikkliste der det er 4 ulike artister, og informasjon innenfor 8 ulike punkter om dem. 
* ### Disse punktene er: 
* #### Artistnavn
* #### Fullt navn
* #### Kjønn
* #### Alder
* #### Fødselsdato
* #### Land
* #### Musikksjanger
* #### Gjennombrudd

* ### Informasjonen til denne listen har jeg fått av ChatGPT, men jeg har skrevet JSON-listen selv. 

* ## Python-Eksempel oppgave 2
1. med <mark> "print(spill[0])"</mark> så printes den første på lista, altså Minecraft. 

2. Når jeg prøvde <mark>"print(spill[2])"</mark> så printet den nummer 3 på lista, som er Fortnite.

3. Når jeg testet <mark>"print(spill[10])"</mark> så fikk jeg feilkoden "list index out of range" fordi det ikke er så mange punkter i listen. 

## Oppgave 4

* Den første vitsen i vitsefilene er "Where do generals keep their armies? In their sleevies!"

* Den siste vitsen i vitsefilene er "There are only 10 types of people in the world: those who understand binary, and those who don't."

* Det er totalt **11** vitser i vitsefilene

* I den første filen står nummeret på vitsen og selve vitsen rett etter hverandre. I den andre filen virker strukturen mer organisert og ryddig. Her kommer det en liten tekst på toppen om hva filen faktisk inneholder, og alle vitsene ligger i en egen liste som heter ```"jokes".``` Hver vits har og fått sin egen ```"id"```.
* Begge vitsefilene inneholder akkurat de samme vitsene, men det er også noen forskjeller. I den første filen er strukturen ganske enkel. Der er hver vits direkte koblet til et nummer, f.eks ```"1": "Where do generals keep their armies?  In their sleevies"```. I den andre filen har vitsene blitt lagt i en egen liste (```"jokes"```). Hver vits har blitt gjort til et objekt, som har både ```"id"``` og ```"joke"```. I den andre filen blir det også forklart hva filen inneholder under ```"metadata"```.