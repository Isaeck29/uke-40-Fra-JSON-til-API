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

* # Oppgave 2

## Python-eksempel
1. med <mark> "print(spill[0])"</mark> så printes den første på lista, altså Minecraft. 

2. Når jeg prøvde <mark>"print(spill[2])"</mark> så printet den nummer 3 på lista, som er Fortnite.

3. Når jeg testet <mark>"print(spill[10])"</mark> så fikk jeg feilkoden "list index out of range" fordi det ikke er så mange punkter i listen. 

## Egen liste
1. Det første elementet i min egen liste er "Minecraft". Om jeg vil printe ut dette kan man bruke ```print(spill[0])```.

2. Det siste elementet i min egen liste er "Counter-Strike". For å printe ut det siste elementet kan man bruke ```print(spill[10])```.

3. Min liste har totalt 11 ulike spill. For å printe ut alle sammen kan man bruke ```print(spill)```.

## Oppgave 4

* Den første vitsen i vitsefilene er "Where do generals keep their armies? In their sleevies!"

* Den siste vitsen i vitsefilene er "There are only 10 types of people in the world: those who understand binary, and those who don't."

* Det er totalt **11** vitser i vitsefilene

* I den første filen står nummeret på vitsen og selve vitsen rett etter hverandre. I den andre filen virker strukturen mer organisert og ryddig. Her kommer det en liten tekst på toppen om hva filen faktisk inneholder, og alle vitsene ligger i en egen liste som heter ```"jokes".``` Hver vits har også fått sin egen ```"id"```.
* Begge vitsefilene inneholder akkurat de samme vitsene, men det er også noen forskjeller. I den første filen er strukturen ganske enkel. Der er hver vits direkte koblet til et nummer, f.eks ```"1": "Where do generals keep their armies?  In their sleevies"```. I den andre filen har vitsene blitt lagt i en egen liste (```"jokes"```). Hver vits har blitt gjort til et objekt, som har både ```"id"``` og ```"joke"```. I den andre filen blir det også forklart hva filen inneholder under ```"metadata"```.
* Toppnivået i begge filene er et objekt. I den første filen er ```"1"```, "```"2"```, ```"3"``` osv. brukt som nummer på de ulike vitsene. I den andre filen har nøklene på toppnivå fått navnene ```"metadata"``` og ```"jokes"```. For å finne en bestemt vits kan man gå inn i listen ```"jokes"``` og finne vitsen ved hjelp av ```"id"```. Hver vits er et eget objekt som har både  ```"id"``` og ```"joke"```.

## Oppgave 5. 
### Jeg har laget et program som kan vise vitsene fra listen med vitser. 
#### Denne koden har en meny, og kan:
* Vise alle vitser fra listen med vitser
* Vise tilfeldige vitser fra listen med vitser
* Vise den første vitsen fra listen med vitser
* Telle antall med vitser som er i listen med vitser
* Søke etter ord som den får med input fra bruker. 
#### Deler av koden i Oppgave 5 er skrevet med hjelp av ChatGPT. 


# Refleksjon

## Hva er JSON?
#### JSON er en måte å lagre informasjon på. Man kan blant annet lage lister, slik som jeg har gjort i filen "musikkliste.json".

## Hvordan er JSON bygget opp?
#### JSON bygges opp av objekter som blir markert med "{ }", lister som blir markert med [] og annen informasjon som består av navn og verdier.

## Hva var lett?
#### Jeg synes at de første 4 punktene var ganske lette.

## Hva var vanskelig?
#### Jeg synes at oppgave 5 var vanskelig, når jeg skulle lage en meny. 

## Hva er forskjellen mellom en lokal JSON-fil og et API?
#### Forskjellen mellom en lokal JSON-fil og et API er at den lokale JSON-fila ligger lagret på min PC, mens med API så ber programmet en annen tjeneste om data. Dette kan f.eks være værmeldingen på YR.no, som API'en henter informasjonen fra via. internett. 