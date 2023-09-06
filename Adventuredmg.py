hp = 100
if hp <=0:
    game_over()
def game_over(): 
    exit()


def rom_1():
    print("Du er i en stor sjukk by. Den hete London. Du e på vei tl butikken.\
    Det e kveld og du ser en fyr med svart hetegenser i en dark alleyway som signaliserer at\
    du burde følge etter han du har 3 valg:")
                 
    valg = input(" A: Du kan gå videre. B: Du kan følge etter han C: Du kan ta opp glocken og blaste han i hode")
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
    valg = input("A: Bare stå der som en vanlig person. B: Ikke gjør noe men vær på vakt C: Du tar opp glocken\
                 D: Du tar opp glocken")
    if valg == "A":
        rom_shank_angrip()
        


def rom_shank_angrip():
    global hp 
    print("han tar opp en kniv det er cirka 2 meter mellomrom mellom dere hva gjør du")
    valg = input("A: Angrip B: Løp C: Dodge og counter attack D: Glock")
    if valg == "A":
        print("Han shanker deg i magen han skal til å drege den ut men du kommer med en right hook rett i skjeven hans\
              ")
        hp-=70
        print("du har", hp, "hp" )
    if valg == "B":
        rom_shank_løp()

def rom_shank_løp():
    global hp
    hp-=50
    print("hp:",hp )

        

def rom_glock1():
    print("du skyter han")
        

    

rom_1()