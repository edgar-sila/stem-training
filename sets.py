from cgi import print_directory
from pyparsing import Word


fruit={"orange","grapes","plums"}
print(fruit)
print(fruit)
print(fruit)

def outputname(a):
    print("hi",a)
outputname("edizo")

#function to replace character in a string
def replace_in(phrase):
    Word=""
    for letter in phrase:
        if letter.lower()in"aeiou":
            word=word +"g"
        else:
            word=word+letter
    return word 
print(replace_in(input("Enter a phrase :")))
#try, except in python to catch errors
try:
    value=int
