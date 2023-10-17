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
