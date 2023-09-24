import random 

hp = 100
if hp > 100:
    hp = 100
Shanker = 100
if Shanker > 100:
    Shanker = 100
# Add chapters å shit
# Add mer RNG
# Husk det viktigste er å vise kompetanse
#Add varjasion i angrepene
The_Art_Of_War_1 = False  # skal settes til false senere, når testing ferdig
Glock = False
TynnShanker = 100
AverageCrowbar = 200
Big_Fyr_Baseball = 500
TynnShankerFight = False
BigFyrBaseballFight = False
AverageCrowbarFight = False
Gunfight = False
Sun_Tzu_The_Art_Of_War_2 = False
rage = 0
Asking = False
def game_over():
    print("Du døde")
    exit()
def Duvant():
    print("-Godamn du vant en vanlig person hadde dratt til legen etter alle skadene. Men du er ikke en normal person så du fortsetter til butta-")
    exit()

def sjekkliv():
    if hp <=0:
        game_over()
        print("Du har ", hp, "hp")
    elif hp > 100:
        print("Du har 100 hp")
def sjekkshanker():
    if Shanker <=0:
        chapter2()

def sjekktynnshanker():
    if TynnShanker <=0:
        chapter2_3T()
def sjekkBigFyrmedbaseballbat():
    if Big_Fyr_Baseball <=0:
        chapter2_3T()
def sjekkAverageCrowbar():
    if AverageCrowbar <=0:
        chapter2_3A()

def velgchapter():
    asking = True
    while asking == True:
        chaptervelger = input("Velg chapter. 1 = Chapter 1. 2 = chapter 2 -")
        if chaptervelger == "A" or chaptervelger == "B":
            asking = False
        else:
            print(" Du skrev feil. Prøv igjen")
    if chaptervelger == "1" or chaptervelger == "A":
        print("-Chapter1-")
        rom_1()
    elif chaptervelger == "2" or chaptervelger == "B":
        print("-Chapter2-")
        chapter2()
    




    
def rom_1():
    print("Du er i en stor sjukk by. Den hete London. Du e på vei til butikken.\
Det e kveld og du ser en fyr med svart hetegenser i en dark alleyway som signaliserer at\
du burde følge etter han du har 3 valg:")
                 
    valg = input(" A: Du kan gå videre. B: Du kan følge etter han C: Du kan ta opp glocken og blaste han i hode -")
    if valg == "A":
        print("Lame")
        exit()
    if valg == "B":
        rom_shank1()
    if valg == "C":
        rom_glock1()

def rom_shank1():
    print("Du følger etter han når dere er gjupt inni THE DARK ALLEYWAY ser du han streker handen sin ned i bukse\
lommen hva gjør du?")
    valg = input("A: Bare stå der som en vanlig person. B: Ikke gjør noe men vær på vakt C: Du tar opp glocken-")
    
    
    if valg == "A":
        print("han tar opp en kniv det er cirka 2 meter mellomrom mellom dere hva gjør du")
        rom_shank2()
    if valg == "B":
        rom_shank2()
        


def rom_shank2():
    global Glock
    Knekk = " "
    global hp 
    global Shanker
    #Add mer gambling forskjellige attacks man gjør når man angriper og damage
    valg = input("A: Angrip B: Løp C:Dodge og counter attack D: Glock -")
    if valg == "A":
        attack_type = random.randint(1, 100)
        if attack_type < 10:
            Attack = "roundhouse kicker"
            tilfeldig_attack = 40
        elif attack_type < 40:
            Attack = "right hooken"
            tilfeldig_attack = 30
        elif attack_type < 60:
         Attack = "left jaba"
         tilfeldig_attack = 15
        elif attack_type < 80:
            Attack = "basic sparker"
            tilfeldig_attack = 25
        elif attack_type < 95:
            Attack = "Biter"
            tilfeldig_attack = 5
        elif attack_type < 100:
            Attack = "Slapper"
            tilfeldig_attack = 70


        



      

        
        tilfeldig_limb = random.randint(1, 100)
        if tilfeldig_limb < 10:
            limb = "nakken"
            tilfeldig_attack *= 2
        elif tilfeldig_limb < 40:
            limb = "chesten"
            tilfeldig_attack *= 1
        elif tilfeldig_limb < 60:
            limb = "Mage"
            tilfeldig_attack *= 1.3
        elif tilfeldig_limb < 75:
            limb = "Beine"
            tilfeldig_attack *= 0.7
        elif tilfeldig_limb < 90:
            limb = "armen"
            tilfeldig_attack *= 0.7
        elif tilfeldig_limb < 99:
            limb = "hode"
            tilfeldig_attack *= 2
        elif tilfeldig_limb == 100:
            limb = "ballan"
            tilfeldig_attack *= 10
            
        
        Shanker -= tilfeldig_attack

        enemy_attack = random.randint(10, 30)

        hp -= enemy_attack
        if tilfeldig_attack < 20:
            Knekk = "gir han et lite blåmerke"

        elif tilfeldig_attack < 30:
            Knekk = " gir han en kraftig blå veis"  

        elif tilfeldig_attack < 50:
            Knekk = "knakk det"
        elif tilfeldig_attack < 100:
            Knekk = "ble KNUST"
        elif tilfeldig_attack > 100:
            Knekk = "ble KNUST"

        

        print("-Du ", Attack, "i", limb, "som ", Knekk,"-" )

        print("du har", hp, "hp" )
        sjekkliv()
        print("Shankeren har ", Shanker, "hp")
        sjekkshanker()
        rom_shank2()

    if valg == "B":
        rom_shank_løp()
        global The_Art_Of_War_1
        global Glock
    if valg == "C":
        if The_Art_Of_War_1 == True:
            print("Han prøver å stabbe deg men etter å ha lest the Art Of War så dukker du unna attacket og bruker (unclassified informasion) til å knuse skallen hans")
            hp-=0
            Shanker-=100
            sjekkliv()
            print("Shankeren har ", Shanker, "hp")
            sjekkshanker()
            rom_shank2()

        else:
            print("Du hakke skillsa du prøver noe annet")
            rom_shank2()
    if valg == "D":
        print("Du tar opp glocken. Shankeren kommer løpenes mot deg. Han closer mellomrommet mellom dere. Du skal til å skyte")
        if Glock == True:

         
            hp-=0
            Shanker-=100
            sjekkliv()
            print("Shankeren har ", Shanker, "hp")
            sjekkshanker()
            rom_shank2()
        else: rom_shank2

def rom_shank_løp():
    global hp
    global Glock
    sjekkliv()
    valg = input("Hva vil du gjøre, A: løpe tilbake, B: leite i søpla -")
    if valg == "A":
        rom_shank2()
    if valg == "B":
        print("du leter i søpla")
        tilfeldigsøppel = random.randint(1, 6)
        if tilfeldigsøppel == 1:
           
            print("Wow en rød sopp med hvite prikker og du er desperat nok til å spise den!")
            hp-=100
            print("hp:", hp)
            print("Han catcher opp med deg dere går i fight igjen")
            sjekkliv()
            rom_shank2()
        if tilfeldigsøppel == 2:
            print("du fant en hel burger så heldig det vi ikke prater om er den brune hundeshiten som ligger oppa den")
            hp+=60
            sjekkliv()
            rom_shank2()
        if tilfeldigsøppel == 3:
            print ("du fant en pakke med pølse. Pølsen er godt inpakket. ")
            print("Du tenker er jeg virkelig så desperat, nei det er du ikke")
            print ("hp", hp)
            sjekkliv()
            rom_shank2()
        if tilfeldigsøppel == 4:
            print("Du ser ikke engang hva det er du bare spiser det")
            randomfoodbuff = random.randint(-100, 100)
            hp -=randomfoodbuff
            sjekkliv()
            rom_shank2()
        if tilfeldigsøppel == 5:
            print("Du fant en side fra den berømte boken. Sun Tzu The Art Of War. På siden står det “Move swift as the Wind and closely-formed as the Wood. Attack like the Fire and be still as the Mountain.”")
            The_Art_Of_War_1 = True
            sjekkliv()
            rom_shank2()
        if tilfeldigsøppel == 6:
            print("Du fant et skudd. Ser ut som den passer til glocken din. ")
            Glock = True
            sjekkliv()
            rom_shank2()

def chapter2():
    chapter_2 = True
    TynnShanker = 100
    AverageCrowbar = 200
    Big_Fyr_Baseball = 500
    print("Shankeren skriker etter at du har troffe han. Sekunder etterpå døde shankeren. Men noen hørte skrike du hører at noen kommer mot deg. Det er cirka tre folk hva gjør du. ")
    print ("De kommer nærmere hva gjør du")
    valg = input("A: Face dem face to face, B: Gjem deg. C: Løp for livet,D: Rop for hjelp")
    print("De kom rundt hjørnet. Det er en tynn man med en shank. Det er en svær man med baseball kølle. Og en ganske average dude som har en crowbar som ser ut som han har noe i lommen.")
    if valg == "A":
        chapter2_1A()
    if valg == "B":
        chapter2_1B()
    if valg == "C":
        chapter2_1C()
    if valg == "D":
        print("Ingen komemr men du ble funnet")
        chapter2_1A()

    



def chapter2_1A():
        print("Du møter dem face mot face. Skal du være mann eller en pyse valget er opp til deg.")
        valg = input("A: Fight B: Løp som faen")
        if valg == "A":
            chapter2_1_5A()
           



        if valg == "B":
            pass
def chapter2_1B():
    print("Du må være rask som faen om du skal rekke å gjeme deg.")
    print("Rundt deg er det flere steder du kan gjeme deg.")
    valg = input("A: Du kan gjeme deg i en liten papboks- B: Du kan gjeme deg i søppla- C: Du kan kravle inn i en åpen vent D: I et skap.")
    if valg == "A":
    
        print("Du passer ikke i den.")
        print ("Det er rett før de kommer rundt gjørnet hva gjør du?")
        valg = input("A: Fight- B: Løp")
        if valg == "A":
            chapter2_1_5A()
    if valg == "B":
        Søppla2()
def Søppla2():
    print("Du gjemmer deg i søppla. Du finner noe!")
    Sun_Tzu_The_Art_Of_War_2 = True
    print("Du fant en side av Sun Tzu The Art Of War på siden står det. In the midst of chaos, there is also opportunity")
    print("Dette kan bli brukbart senere")
    print("Den tynne shankeren lener seg inntil søppelkassa du befinner deg i. Hva gjør du?")
    valg = input("A: Sneak Attack. B: Hopp ut og løp")
    if valg == "A":
        print("Du skal til å sneak attacke")
        random = random.randint(1, 3)
        if random == 3:
            print("Du ble catcha ser ut som at du må¨fighte fair and square")
            hp =-30
            print("Du mista 30 hp")
            print("Du har", hp, "hp")
            sjekkliv()
            chapter2_2_5AF()

        else: print("Sneak attack var en suksess. Du drepte shankeren instantly.")
        chapter2_3T()


    
def chapter2_1C():
    pass
def chapter2_1_5A():
    global TynnShankerFight, AverageCrowbarFight, BigFyrBaseballFight
    valg = input("Hvem vil du fighte? A: tynn man med shank. B: Big guy med baseball bat. C: Average dude med crowbar? ")
    if valg == "A":
        TynnShankerFight = True
        chapter2_2_5AF()
    if valg == "C":
        AverageCrowbarFight = True
        chapter2_2_5AF()
    if valg == "B":
        BigFyrBaseballFight = True
        print("Du løper mot den tynne mannen. De tror han er nok til å ta deg alene. Så han fighter solo mens de andre ser på")
        chapter2_2_5AF()
def chapter2_2_5AF():
    Knekk = " "
    global hp 
    global TynnShanker
    global AverageCrowbar
    global Big_Fyr_Baseball
    global TynnShankerFight
    global enemy_attack


    valg = input("A: Angrip B: Løp C:Dodge og counter attack D: Glock -")
    if valg == "A":
        attack_type = random.randint(1, 100)
        if attack_type < 10:
            Attack = "roundhouse kicker"
            tilfeldig_attack = 40
        elif attack_type < 40:
            Attack = "right hooken"
            tilfeldig_attack = 30
        elif attack_type < 60:
         Attack = "left jaba"
         tilfeldig_attack = 15
        elif attack_type < 80:
            Attack = "basic sparker"
            tilfeldig_attack = 25
        elif attack_type < 95:
            Attack = "Biter"
            tilfeldig_attack = 5
        elif attack_type < 100:
            Attack = "Slapper"
            tilfeldig_attack = 70

        
        tilfeldig_limb = random.randint(1, 100)
        if tilfeldig_limb < 10:
            limb = "nakken"
            tilfeldig_attack *= 2
        elif tilfeldig_limb < 40:
            limb = "chesten"
            tilfeldig_attack *= 1
        elif tilfeldig_limb < 60:
            limb = "Mage"
            tilfeldig_attack *= 1.3
        elif tilfeldig_limb < 75:
            limb = "Beine"
            tilfeldig_attack *= 0.7
        elif tilfeldig_limb < 90:
            limb = "armen"
            tilfeldig_attack *= 0.7
        elif tilfeldig_limb < 99:
            limb = "hode"
            tilfeldig_attack *= 2
        elif tilfeldig_limb == 100:
            limb = "ballan"
            tilfeldig_attack *= 10
        #forskjellige enemies gjør forskjellig damage
            
        print("-Du ", Attack, "i", limb, "som ", Knekk,"-" )
        print("du gjorde", tilfeldig_attack, "dmg")
        if TynnShankerFight == True:
            TynnShanker -= tilfeldig_attack
            enemy_attack = random.randint(10, 30)
        print("Shankeren har ", TynnShanker, "hp")
        if BigFyrBaseballFight == True:
            Big_Fyr_Baseball -= tilfeldig_attack
            enemy_attack = random.randint(20, 40)
            print("Baseballbat fyren har ", Big_Fyr_Baseball, "hp")
        if AverageCrowbarFight == True:
            AverageCrowbar -= tilfeldig_attack
            enemy_attack = random.randint(20, 40)
            print("Crowbar fyren har ", AverageCrowbar, "hp")

        

        hp -= enemy_attack
        if tilfeldig_attack < 20:
            Knekk = "gjør at han får et lite blåmerke"

        elif tilfeldig_attack < 30:
            Knekk = " gjør han får en kraftig blå veis"  

        elif tilfeldig_attack < 50:
            Knekk = "knakk det"
        elif tilfeldig_attack < 100:
            Knekk = "ble KNUST"
        elif tilfeldig_attack > 100:
            Knekk = "ble KNUST"



        print("du har", hp, "hp" )
        sjekkliv()
        sjekktynnshanker()
        sjekkBigFyrmedbaseballbat()
        sjekkAverageCrowbar()
    
        chapter2_2_5AF()
def chapter2_3T():
    global hp
    print("Du drepte Shankeren. De to andre står der i shock. Men snapper ut av det. Forvirrheten deres blir raskt om til sinne.")
    print("Han average fyren med crowbar tar opp en glock")
    valg = input("Hva gjør du? A: Dodge B: Finn cover C: Løp D:")
    if valg == "A":
     print("Han holder pistolen mot deg. Han regnet med at du skulle snu rundt å løpe. Men du står der klar for å dukke unda rett før han skyter. Du prøver å lese bodylanguagen hans:")
     print("Han legger fingeren sin på triggern. Han PRESSER INN")
     valg = input("A: Dodge B: Stå i ro")
     if valg == "A":
        print("Du hiver deg på bakken. Men han skøyt ikke når du trodde han ville. Du prøver å røyse deg men... Du hører et høyt BANG. Du driver å svimer av. Du blir plukket opp og hivet i søppla der du blør ut")
        hp = 0
        sjekkliv()
    if valg == "B":
        chapter2_3_2T()
def chapter2_3_2T():
    print("Han har pistolen klar mot hjerte ditt. Han stryker avtrekkeren. The tension rises. BOOOOOOOOMMMMMM!!!")
    valg = input("A: Dodge B: Stå i ro")
    if valg == "A":
        print("Boome var en katt som dyttet ned et søppel lokk")
        print("Du hiver deg på bakken. Men han skøyt ikke når du trodde han ville. Du prøver å røyse deg men... Du hører et høyt BANG. Du driver å svimer av. Du blir plukket opp og hivet i søppla der du blør ut")
        hp = 0
        sjekkliv()
    if valg == "B":
        print("Boome var en katt som rivde ned et søppelkasse lokk")
        print("Igjen han skøyt ikke")
        chapter2_3_3T()
def chapter2_3_3T():
    print("Han puster inn")
    valg = input("A: Dodge B: Stå i ro")
    if valg == "A":
        print("Du hiver deg på bakken. Men han skøyt ikke når du trodde han ville. Du prøver å røyse deg men... Du hører et høyt BANG. Du driver å svimer av. Du blir plukket opp og hivet i søppla der du blør ut")
    hp = 0
    sjekkliv()
    if valg == "B": 
        print("Du ble ikke skutt")
    chapter2_3_4T()  


def chapter2_3_4T():
    global hp
    print("Han holder pusten")
    valg = input("A: Dodge B: Stå i ro")
    if valg == "A":
        print("Du hiver deg på bakken. Men han skøyt ikke når du trodde han ville. Du prøver å røyse deg men... Du hører et høyt BANG. Du driver å svimer av. Du blir plukket opp og hivet i søppla der du blør ut")
        hp = 0
        sjekkliv()
    if valg == "B":
        print("Du ble ikke skutt")
        chapter2_3_5T()
def chapter2_3_5T():
    global hp
    print("Han puster ut")
    valg = input("A: Dodge B: Stå i ro")
    if valg == "A":
        chapter2_3_6T()
    if valg == "B":
        print("Han skyter deg. Du burde dukket unna. Han traff deg rett i hjerte.")
        hp = 0
        sjekkliv()
def chapter2_3_6T():
    print("Du hopper unna og hører et høyt BANG! Recoilen fra pistolen gir deg cirka et sekund lengre tid.")
    valg = input ("Hva vil du gjøre? A: Finn cover B: Make a run for it C: Angrip")
    if valg == "A":
        print("Du har flere steder å gjeme deg.")
        valg = input("Du kan gjemme deg i A: en søppelkasse, B: Et skap C: En halv bil")
        if valg == "A":
            Søppel3()
def Søppel3():
    global Sun_Tzu_The_Art_Of_War_2
    print("Du kan lete i søppelkassen etter shit")
    tilfeldig = random.randint(1, 6)
    if tilfeldig == 1:
        print(" Du fant en klokke")
        print(" Klokken er 3 på natta")
    if tilfeldig == 2:
        print("Du fant et pizzastykke")
        hp+=50
        print("Du har", hp, "hp")
    if tilfeldig == 3:
        print("Du fant et egg")
        hp-=1
        print("Du mistet 1 hp")
        print("Du har", hp, "hp" )
        sjekkliv()
    if tilfeldig == 4:
        print("Du fant en juicy lasagne på bunen av søppelkassa, den er litt grønn men hvem sier nei til lasagne!")
        hp = 100
    if tilfeldig == 5:
        print("Du hadde ikke lyst å lete")
    if tilfeldig == 6:
        print("Du fant en side av Sun Tzu The Art Of War, på siden står det In the midst of chaos, there is also opportunity")
        Sun_Tzu_The_Art_Of_War_2 = True

    chapter2_4Søppel()
def chapter2_4Søppel():
    print("Du er i søppelkassa med lokket igjen. Du prøver å åpne det men det går ikke opp. Du hører latter fra toppen av søppelkassen")
    chapter2_4Søppel2()
def chapter2_4Søppel2():
    print("Crowbar kødden sitter på toppen av søppelkassa og ler")
    valg = input("Hva vil du gjøre? A: Prøve å sparke den opp, B: Tenk på alle tabbene du noen gang har gjort.")
    if valg == "A":
        Søppelspark()
    if valg == "B":
        valg = input("Hva vil du gjøre? A: Tenk på gangen du glemte lummeboka. B: Tenk på gangen du fikk et popkorn stuck mellom tennene dine ")
        rage = 1
        print("Du blir sur")
        valg = input("A: Du kan tenke på gangen foreldrene dine glemte å plukke deg opp fra citynord da du var 9 B: Den jævla headsett kabelen")
        if valg == "A":
            rage += 1
            print("Du blir enda litt surere")
        if valg == "B":
            print("Du e ganske jævla sur")
        valg = input("A: Tenk på Overwatch 2 B: Tenk på gangen du tråkka i vann med sokkan på")
        if valg == "A":
            rage += 4
            print("Du fikk lyst å shank noen")
            
        if valg == "B":
            rage += 3
            print("Du ble veldig sur")
        Søppelspark()


def Søppelspark():
    rage = 10
    if rage < 5:
        print("Du prøver å sparke den opp men det går ikke")
        print("Du prøver å sparke den opp i cirka 5 minutter uten lykke. ")
        print(" Fyren på toppen går lei og det siste du hører er: ASTA LAVISTA BABY!")
        hp = 0
        sjekkliv()
        chapter2_4Søppel()
    elif rage >= 5:
        print("Du bruker alt sinne ditt til å sparke opp det jævla søppel lokket. Som launcher den jævla kukshiten som satt på lokket opp i luften")
        print("Og rett ned på bakken foran deg. Han mistet busten etter å lande på bakken med ryggen først")
        valg = input("Du kan A: Ta en del av et knust fat. B: Eller ikke")
        if valg == "A":
            print("Baseball bat køden står en del unna og fyren som hadde crowbaren. Er den som ligger på bakken foran deg.")
            print("Baseball bat duden løper i mot deg for å reddet bro-en sin men han vil ikke rekke det i tide.")
            print("Du tar det knuste fate og skal til å stabbe crowbarduden med det.")
            print("Men så sier han. Are you gonna stab me with that broken piece of plate.")
            print("Du er 5 centimeter unna å treffe han når du realizer at dette er en breaking bad refrence.")
            valg = input("Hva gjør du? A: Lar han leve. B: Ikke la han leve")
            if valg == "A":
                print("Du lar han leve. Og dere alle stopper å fighte. Siden dere alle har sett breaking bad.")
                Duvant()
            if valg == "B":
                print("Bro har sett breaking bad kordan våga du")







  
def chapter2_3A():
    pass
def chapter2_3B():
    pass


        
    

        

def rom_glock1():
    print("du skyter han")
        

    
velgchapter()
