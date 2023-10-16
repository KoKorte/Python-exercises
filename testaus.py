#variable for vartest
vartest = 7
#simple hello world test
print("Hello World!")

#one line comment test
"""
multi line comment test
"""

#
#variable test
#
print("Let's print vartest variable", vartest)

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

#
#separator test
#
print("Hello","World!", sep=" ")

#
#list test
#
mylistA = ["Minä", "olen", "Niko"]

print(mylistA)
print(type(mylistA))

mylistA[0] = "Hei"
print(mylistA)
