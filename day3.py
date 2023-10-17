"""
PYTHON 103
==========

Tavoitteet:
-Ymmärtää erilaiset muuttujat
-Ymmärtää tietotyypit eli millaisia asioita voi tallettaa erilaisiin muuttujiin
-Ymmärtää mitä tarkoittaa string, integer ja floating point number

KERTAUS

Kysytään miten muuttujat, input ja print toimivat...

Muuttujat eivät ole välttämättä aina merkkijonoja vaan ne voivat olla numeroita

luku1 = 100
luku2 = "100"

print(luku1)
print(luku2)

f merkkijonolla tulostus

tulos = 111 * 2
print(f"Tulos: {tulos}")

Tehtävä 103-1: Kirjoita ohjelma, joka tulostaa seuraavan f-merkkijonoilla
Hei olen etunimi sukunimi ja olen X-vuotias.

Liukulukujen (float) toiminta

luku1 = 1.23
luku2 = -2.34
luku3 = 3.45

keskiarvo = (luku1 + luku2 + luku3) / 3
print(f"Keskiarvo: {keskiarvo}")

Tehtävä 103-1: Kirjoita ohjelma, jossa on kaksi muuttujaa x = 123 ja y = 456

Se tulostaa
x + y =
x - y =
x * y =
x / y =
"""
#Let's print "starting line"
print("\n#################\n")
print("START")
print("\n#################\n")
#
#1: Kirjoita ohjelma, joka tulostaa seuraavan f-merkkijonoilla
#Hei olen etunimi sukunimi ja olen X-vuotias.
#
namea = input("Please, enter your name: ")
nameb = input("Now, enter your surname: ")
age = int(input("And your age: "))


print(f"Hei olen {namea} {nameb} ja olen {age}-vuotias.")

print("\n#################\n")
#
#2: Kirjoita ohjelma, jossa on kaksi muuttujaa x = 123 ja y = 456
#
x = 123
y = 456
sum = x + y
diff = x - y
mul = x * y
div = x / y

print(f"\nx + y = {sum} \nx - y = {diff} \nx * y = {mul} \nx / y = {div}")
