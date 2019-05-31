import random, os, time #importerar funktioner(random, omstart och en delay function)

tot = [] 
rtot = [] 
röst = [] 
a = 0
b = 0
omstart = True

class Partier: #En klass som jag använder för att lägga in alla partier
    def __init__(self, name, inriktning, minr, maxr, partiledare, uttalandeV, uttalandeF): #definerar det sätt som värdena ska skrivas in som
        self.name = name #sätter variablar för varje värde  i klassen. just denna är fö namnet
        self.inriktning = bool(inriktning) #en bool variabel som avgör inriktningen
        self.minr = int(minr) #minsta antal röster som ett parti kan få
        self.maxr = int(maxr) #största antal röster som ett parti kan få
        self.partiledare = partiledare #namnet på partiledaren
        self.uttalandeV = uttalandeV #uttalande om partiet får mycket röster
        self.uttalandeF = uttalandeF #uttalande om partiet får lite röster
        if inriktning == True: #en if-loop som avgör vilken inriktning partiet har utifrån inriktningsvariabeln
            self.inriktning = "Vänster"
        else:
            self.inriktning = "Höger"
        
parti1 = Partier("Gröngölingarna", False, 3, 12, "Jonas Ostbåge", "Jag trodde aldrig att detta kunde ske!", "Jag är mycket nöjd med resultatet") #Här anger jag de olika variablerna för varje parti. Uteformat efter klassens struktur
parti2 = Partier("Partikelpartiet", False, 2, 8, "Hans Majonäs", "Inte riktigt det resultat vi hoppades på.", "Vi tycker att detta är ett fantastikt resultat!")
parti3 = Partier("Mälarpartiet", True, 8, 18, "Pernilla Godisgorilla", "Det är inte möjligt!!!", "Ett bra resultat men det kan förbättrs")
parti4 = Partier("SJörövarpartiet", True, 3, 12, "Arja Samerna", "Detta var en stor besvikelse.", "Viktiga procent för oss, vi är nöjda")
parti5 = Partier("Extremisterna", True, 3, 6, "Lenart Lurig", "Känns tråkigt men vi hade inga höga förväntningar", "Resultatet är vi mycket nöjda med.")
parti6 = Partier("Maskinpartiet", False, 12, 22, "Robert Rostbiff", "Verkligen inte vad vi hade trott", "Jag tror att detta kommmer att räcka långt.")
parti7 = Partier("Framtidspartiet", True, 12, 18, "Antwon Släp", "Nej men va i hela faaaaaan!", "JAAAAAAAAA!!, vi är fan bäst")
parti8 = Partier("Fotbollspartiet", False, 20, 34, "Dan Dan", "Inte riktigt vad vi hade hoppats på.", "Yesss vinnare igen!!")

rösterG = random.randint(parti1.minr, parti1.maxr)#Här tar vi ut ett random värde mellan det största opch minsta värdet som partiet kan får. 
röst.append(rösterG)#Denna raden lägger till värdet som vi fick fram i en array där jag sparar alla röster
rösterP = random.randint(parti2.minr, parti2.maxr)#Samma sak fast för parti2, osv
röst.append(rösterP)#Lägger till värdet för parti2, osv
rösterMP = random.randint(parti3.minr, parti3.maxr)
röst.append(rösterMP)
rösterS = random.randint(parti4.minr, parti4.maxr)
röst.append(rösterS)
rösterE = random.randint(parti5.minr, parti5.maxr)
röst.append(rösterE)
rösterM = random.randint(parti6.minr, parti6.maxr)
röst.append(rösterM)
rösterF = random.randint(parti7.minr, parti7.maxr)
röst.append(rösterF)
rösterFB = random.randint(parti8.minr, parti8.maxr)
röst.append(rösterFB)

rösterOLJ = rösterE + rösterM + rösterF#Här lägger jag ihop alla röster för de partier som är med i oljeblocket
rösterSMÅ = rösterG + rösterP + rösterMP + rösterS#Här lägger jag ihop alla röstert för Småpartierna
rösterTot = rösterOLJ + rösterSMÅ + rösterFB#Här lägger jag ihop alla partiers röster

if rösterTot > 100: #Den här if-loopen gör så att om alla röster sammanlagt blir över 100% så ska programmet startas om
    time.sleep(1) #Den här är en funktion i "time" biblioteket som jag importerade. Den sätter ett delay på 1 sekund
    print("Ryskt val, mer än 100% röstade.") #Print funktionen skriver ut det som står inanför paranteserna i terminalen
    print("Valet startar om.")
    print("...")
    omstart = False #Här sätter jag en variabel till false vilket är viktigt längre ner i koden
    os.system("python Val2022.py") #Det här är också en funktion som jag importerade och det är den som startar om programmet (import os)
else: #Här säger vi vad som ska hända om vi inte fick över 100%
    time.sleep(1) #Här har vi delay funktionen igen
    print(str(rösterTot) + "% röstade.") #Man inte skriver texten som man vill skriva ut inom kaninöron("") så kommer prgrammet att skriva ut en variabel med det namnet. Också behövde jag göra om variabeln till en string för att kunna skriva ur den med resten

if omstart == True: #Här kollar den om variablen "omstart"=true och det betyder att vi inte har mer än 100% röster
    if rösterG > 3: #Dessa if-loopar kollar om varje parti har minst 4% av rösterna annars kommer de inte med i valet
        tot.append("Gröngölingarna") #Lägger till partinamnet i en array
        rtot.append(rösterG)#Lägger till partiets röster i en array

    if rösterP > 3: #Kollar för pareti2. Det som står inanför if-loopen sker bara om rösterna är större än 4%
        tot.append("Partikelpartiet")#Lägger till partinamn2, osv
        rtot.append(rösterP)#Lägger till parti2's röster, osv

    if rösterMP > 3:
        tot.append("Mälarpartiet")
        rtot.append(rösterMP)

    if rösterS > 3:
        tot.append("Sjörövarpartiet")
        rtot.append(rösterS)

    if rösterE > 3:
        tot.append("Extremisterna")
        rtot.append(rösterE)

    if rösterM > 3:
        tot.append("Maskinpartiet")
        rtot.append(rösterM)

    if rösterF > 3:
        tot.append("Framtidspartiet")
        rtot.append(rösterF)

    if rösterFB > 3:
        tot.append("Fotbollspartiet")
        rtot.append(rösterFB)

    time.sleep(0.5),print("..."),time.sleep(0.5),print("..."),time.sleep(0.5),print("..."),time.sleep(0.5),print("..."),time.sleep(1.5)#Här lägger vi till ettdelay mellan varje rad vi skriver. Detta får det att se ut som att programmet arbetar med rsultatet

    for i in tot: #Här kollar for-loopen för varje parti i parti-arrayen hur många röster varje parti har
        print(str(i), "fick", str(rtot[b]) + "% av rösterna") #Skriver ut partinamn och partiets röster
        time.sleep(0.5)#Sätter ettt delay på 0.5 sekunder
        b = b + 1 #ökat variablen i printfunktionen för att den ska skriva ut nästa värde i tabellen

    print("---------------------------------") 
    time.sleep(0.5)
    print("Oljeblocket hade", str(rösterOLJ) + "% av rösterna")#Här skriver vi ut procentuella antalet röster för Oljeblocket
    time.sleep(0.5)
    print("SMåpartierna hade", str(rösterSMÅ) + "% av rösterna")#Här skriver vi ut procentuella antalet röster för Småpartierna

    störstRTOT = max(rtot) #här kollar vi vilket värder i röst-arrayen som var störst

    for i in rtot: #Kär så många gånger sopm det finns partier i röst-arrayen
        if störstRTOT == rtot[a]: #Denna loop kollar vilket av partiernas röster som matchar med värdet som vi fick ut när vi tog största värdet
            print(tot[a]+ " vann valet med " +str(rtot[a])+ "%") #Här skriver vi sedan ut partinamnet och rösterna för det partiet
        else: #Här säger vi vad som ska hända om partiets röster inte matchade med värdet
            a=a+1 #Lägger till 1 till variable så att nästa gång loppen körs så lolla  vi nästa partis röster

    print("---------------------------------") #Priont funktionen igen
    print("Här kommer några uttalanden från partiledarna: "), time.sleep(1) #Delay på 1 sekund
    if 3 < rösterG and rösterG> 6: #Dessa if-loopar avgör vilket uttalande som ska skrivas ut
        print(parti1.name+" - "+parti1.uttalandeV), time.sleep(0.5) #Skirvar ut partiets namn + partiets uttalande om det gick bra
    else:
        print(parti1.name+" - "+parti1.uttalandeF), time.sleep(0.5) #Skriver ut partiets namn + partiets uttalande om det gick dåligt
    if 3 < rösterP and rösterP > 5:
        print(parti2.name+" - "+parti2.uttalandeV), time.sleep(0.5) #Samma för parti2, osv
    else:
        print(parti2.name+" - "+parti2.uttalandeF), time.sleep(0.5) #Samma för parti2, osv
    if 3 < rösterMP and rösterMP> 11:
        print(parti3.name+" - "+parti3.uttalandeV), time.sleep(0.5)
    else:
        print(parti3.name+" - "+parti3.uttalandeF), time.sleep(0.5)
    if 3 < rösterS and rösterS > 6:
        print(parti4.name+" - "+parti4.uttalandeV), time.sleep(0.5)
    else:
        print(parti4.name+" - "+parti4.uttalandeF), time.sleep(0.5)
    if 3 < rösterE and rösterE > 4:
        print(parti5.name+" - "+parti5.uttalandeV), time.sleep(0.5)
    else:
        print(parti5.name+" - "+parti5.uttalandeF), time.sleep(0.5)
    if 3 < rösterM and rösterM > 15:
        print(parti6.name+" - "+parti6.uttalandeV), time.sleep(0.5)
    else:
        print(parti6.name+" - "+parti6.uttalandeF), time.sleep(0.5)
    if 3 < rösterF and rösterF> 14:
        print(parti7.name+" - "+parti7.uttalandeV), time.sleep(0.5)
    else:
        print(parti7.name+" - "+parti7.uttalandeF), time.sleep(0.5)
    if 3 < rösterFB and rösterFB > 25:
        print(parti8.name+" - "+parti8.uttalandeV), time.sleep(0.5)
    else:
        print(parti8.name+" - "+parti8.uttalandeF), time.sleep(0.5)
else:
    a=0 #Sätter bara en varablen till 0 för att programmet måste ha något att göra. Detta göller bar vi omstart när programmet har fått över 100%
