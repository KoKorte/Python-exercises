"""
PYTHON 102
==========

Tavoitteet:
-Osaa tehdä ohjelman, joka lukee käyttäjän tekemän tekstin ja tulostaa sen näytölle
-Ymmärtää mitä muuttujat ovat
-Osaa yhdistää erilaisia merkkijonoja ja muuttujia

Syöttö tapahtuu input komennolla

tulos = input("Kirjoita jotain")
print("Kirjoitit tekstin " + tulos)

Muuttujan nimi voi olla periaatteessa mitä tahansa. Käytännössä sen pitää olla kuvaava.
input komento voi käyttää samaa muuttujaa ja näin käyttää yhtä muuttujaa usean kerran.
Muuttujaa voi käyttää monta kertaa ohjelmassa ja sille voi antaa uuden arvon.
Muuttuja ja olemassa oleva merkiijonon yhdistäminen voidaan tehdä monta kertaa.

Tehtävä 102-1: Kirjoita ohjelma, joka kysyy oman nimesi ja tulostaa sen.

Tehtävä 102-2: Kirjoita ohjelma, joka kysyy oman nimesi kerran ja tulostaa sen kahdesti.

Tehtävä 102-3: Kirjoita ohjelma, joka kysyy kaksi kertaa nimen ja tulostaa sitten annetun nimen.

Tehtävä 102-4: Kirjoita ohjelma, joka kysyy nimen ja tulostaa jonkin erikoismerkin ja nimen ja toisen erikoismerkin.
Esimerkiksi: !Aapeli@

Ohjelmassa voi olla monta muuttujaa ja tulostuksessa voidaan käyttää useita muuttujia.

Tehtävä 102-5: Kirjoita ohjelma, joka kysyy etunimen ja sukunimen ja kirjoittaa "nimesi on <etunimi> sukunimi>."

Tehtävä 102-6: Kirjoita ohjelma, joka kysyy nimesi ja osoitteesi ja tulostaa sen kuten osoite kirjoitetaan kirjeessä

BONUS
=====

Tehtävä 102-7: Kirjoita ohjelma, joka kysyy 2-3 asiaa ja tulostaa lyhyen muutaman rivin tarinan, jossa näitä asioita on käytetty.
"""
#Let's print "starting line" and add task number before every task
print("\n#################\n")
print("START")
print("\n#################\n")
#
#1: Kirjoita ohjelma, joka kysyy oman nimesi ja tulostaa sen.
#
print("TASK 1.")
name = input("Please, enter your name: ")
print("Hello, ", name)

print("\n#################\n")
#
#2: Kirjoita ohjelma, joka kysyy oman nimesi kerran ja tulostaa sen kahdesti.
#
print("TASK 2.")
namename = input("Please, enter your name: ")
print("Hello, ",namename *2)

print("\n#################\n")
#
#3: Kirjoita ohjelma, joka kysyy kaksi kertaa nimen ja tulostaa sitten annetun nimen.
#
print("TASK 3.")
nameone = input("Please, enter your name: ")
nametwo = input("Please, repeat that: ")

print(nameone + nametwo)

print("\n#################\n")
#
#4: Kirjoita ohjelma, joka kysyy nimen ja tulostaa jonkin erikoismerkin ja nimen ja toisen erikoismerkin.
#Esimerkiksi: !Aapeli@
#
print("TASK 4.")
name4 = input("Please, enter your name: ")

print("|"+name4+"|")

print("\n#################\n")
#
#5: Kirjoita ohjelma, joka kysyy etunimen ja sukunimen ja kirjoittaa "nimesi on <etunimi> sukunimi>.
#
print("TASK 5.")
name5a = input("Please, enter your firstname: ")
name5b = input("Now enter your surname: ")

print("Your name is: ", name5a , name5b)

print("\n#################\n")
#
#6: Kirjoita ohjelma, joka kysyy nimesi ja osoitteesi ja tulostaa sen kuten osoite kirjoitetaan kirjeessä.
#
print("TASK 6.")
name6a = input("Please, enter the firstname: ")
name6b = input("Now, enter the surname: ")
address6a = input("Now, enter the address: ")
postal6a = input("And the postal code: ")
city6a = input("Last, the name of the city: ")

print("The letter you want to send is set to following address: ", "\n",name6a, name6b,"\n",address6a,"\n",postal6a , city6a)

print("\n#################\n")
#
#7: Kirjoita ohjelma, joka kysyy 2-3 asiaa ja tulostaa lyhyen muutaman rivin tarinan, jossa näitä asioita on käytetty.
#
print("BONUS TASK 7.")
q1 = input("Give me a name: ")
q2 = input("Give me a verb: ")
q3 = input("Give me a mood: ")

print("Once upon a time, when ",q1,"was",q2,"while being",q3)
