print ("Du er i en hule og møter en vild Shaman Durek")
def rom_1():
    
    valg = input("Hva gjør du? A: Slåss B: Løp")
    if valg == "A":
        print("Det var en hard kamp men du kom ut i livet")
        rom_2()
    elif valg == "B":
        print("Ingen kan løpe fra Shaman Durek! Du er død")    
    else:
        print ("Dette var ikke et valg så du døde")


def rom_2():
         print ("Du går videre... Du går lengre i inn i hulen. Du møter Truls hva gjør du")
         valg = input("1: Prøv å bli venner som Ole bromm sier en fremmed er venn du aldri har møtt! 2: Du gjør en trippel dropkick. 3: Du tar en rask uppercut")
         if valg == "1": 
            print == ("Først så trur du at dere har blitt venner men når dere skal til å gå videre skjenner du en spøyte i ryggen.")
         if   valg == "2":
            print("Du treffer han i skjeven. Dette knocker han ut")
         if valg == "3":
            print ("Du slo pusten ut av men han tar ut en sprøyte og stikker deg i låret med en sprøyte før du rekker å slå han en gang til")
def rom_Kjelder():
    print ("Du våkner i Truls kjeller du er i håndjern og er bundet til en stol. Truls kommer inn med et glis. Hva han bir å gjøre med deg. Det er ting jeg ikke kan nevne her. Han går ut og mister et par nøkkler ut av baklommen. Hva gjør du?")
    valg = input("A: Du venter B: Du strekker ut foten for å få tak i nøkkelen. C: Det er en ovn bak deg du kan prøve å brenne tauet som holder deg fast")
    if valg == "A":
        print()
        
rom_1()




