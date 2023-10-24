import copy

#variable for vartest
vartest = 7
print("#################\nSTART\n#################")
print("\n#################\n")
#simple hello world test
print("Hello World!")

print("\n#################\n")
#one line comment test
"""
multi line comment test
"""

print("\n#################\n")
#
#variable test
#
print("Let's print vartest variable", vartest)

print("\n#################\n")
#
#multi line test
#
print(
"""
Line
test
"""
)
print("""\nLine\ntest\n""")

print("\n#################\n")
#
#separator test
#
print("Hello","World!", sep=" ")

print("\n#################\n")
#
#list test
#
mylistA = ["Minä", "olen", "Niko"]

print(mylistA)
print(type(mylistA))

mylistA[0] = "Hei"
print(mylistA)

print("\n#################\n")
#
#bit test
#

print("\n#################\n")
#
#if test
#
inputnum = int(input("\nGive me a number and let's see if it is even or odd: "))

if inputnum % 2 == 0:
    print("\nNumber is even")
else:
    print("\nNumeber is odd")

print("\n#################\n")
#
#range test
#
rangelist = [111,222,333,444,555,666,777,888,999]
for index in range(0,len(rangelist),1):
    print(rangelist[index], end=" ")

print("\n#################\n")
#
#while test
#
testnumber2 = 0
while testnumber2 < 10:
    testnumber2 += 2
    print(testnumber2, end=" ")
else:
    print("while test end")

print("\n#################\n")
#
#concatenate (list merge)
#
aaa = [17]
bbb = [10]
ccc = [2023]

ddd = aaa + bbb + ccc
print(ddd)

print("\n#################\n")
#
#deepcopy test
#
testlistB = [1,2,3]
testlistA = [4,5,6]

testlistB = copy.deepcopy(testlistA)
testlistA[0] = 111
print(testlistA)
print(testlistB)

print("\n#################\n")
#
#looping dictionary
#
"""
for key in mydictCCC:
    print(key, mydictCCC[key])
"""

#
#class test
#
class Eläin:
    def __init__(self) -> None:
        pass

class Kokeilu:
    def __init__(self) -> None:
        pass

    def testi(self):
        print("Kokeilu")

class Eläin (Kokeilu):
    def __init__(self) -> None:
        super().__init__()

    def testi(self):
        print("Eläin")

class Auto (Kokeilu):
    def __init__(self) -> None:
        super().__init__()

    def testi(self):
        print("Auto")

class Kissa (Eläin, Auto):
    def __init__(self) -> None:
        super().__init__()

kissa = Kissa()
kissa.testi()

auto = Auto()
auto.testi()

kokeilu = Kokeilu()
kokeilu.testi()

eläin = Eläin()
eläin.testi()

lista = [kokeilu,eläin,kissa,auto]
for i in lista:
    i.testi()

#
#class test 2
#
class ExampleA:
    variableclass = 1234
    variableinstance = 4567

    def __init__(self, arg):
        self.variableinstance = arg
        ExampleA.variableclass = arg

print(ExampleA.variableclass)

ex1 = ExampleA(1111)
ex2 = ExampleA(2222)
print(ex1.variableclass, ex2.variableclass)
print(ex1.variableinstance, ex2.variableinstance)
ex2.variableinstance = 9999
print(ex1.variableclass, ex2.variableclass)
print(ex1.variableinstance, ex2.variableinstance)
