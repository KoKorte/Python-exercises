#NUMBER GUESSING GAME

#REQUIREMENTS:
"""
-guess a number between 1-100 (range of accepted inputs)
-print(random.randrange(1,101))
-to win the number has to be same as a secret number
-import random
-10 wrong answers and the game is lost
-restart after game ends (RESTART? Y and N: )?
"""

import random

def numberguessing():
    random.seed()

    secretnumber = random.randrange(1, 101)
    fails = 10

    print("---------------------------------------------")
    print("----------------TERVETULOA-------------------")
    print("---------------------------------------------")

    print("ARVAA NUMERO 1 ja 100 VÄLILLÄ OIKEIN")
    print("SAAT 10 YRITYSTÄ!")
    print("---------------------------------------------")

    for fails in range(1, fails + 1):
        guess = int(input(f"Syötä luku: "))

        #Tarkistetaan että syöttö oli "laillinen"
        if guess < 1 or guess > 100:
            print("SYÖTÄ NUMERO 1 JA 100 VÄLILLÄ!!!")
            continue

        if guess < secretnumber:
            print("Väärin, yritä uudelleen!")
            print("---------------------------------------------")
        elif guess > secretnumber:
            print("Väärin, yritä uudelleen!")
            print("---------------------------------------------")
        else:
            print(f"Oikein. Oikea numero oli kuin olikin {secretnumber}!")
            break
        
        #Tarkistetaan onko arvattu numero viiden luvun päässä oikeasta
        close = abs(secretnumber - guess)
        if close <= 5:
            print("Uuuu! Nyt alkaa polttamaan!")
    
    #Tulostaa häviön liian monen yrityksen jälkeen
    else:
        print(f"Liian monta yritystä! Oikea luku oli: {secretnumber}")

#Tarkistetaan haluaako pelaaja vielä pelata
while True:
    numberguessing()
    restart = input("Haluatko pelata uudestaan? Kyllä(Y) tai Ei(N): ").strip().lower()
    if restart != "y":
        break
