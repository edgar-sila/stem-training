#dictionries in python
mydict={
    "book":"dynamics",
    "publishers":"longhorn",
    "year":2001
        }

#accesing item.
x=mydict['year']
print(x)
#accesing using get()
y=mydict.get('book')
print(y)
#all keys
x=mydict.keys()
print (x)
#all values.
x= mydict.values()
print(x)
#printing all items in a dictionary
x=mydict.items()
print(x)
#cheking if key exist
if "publisher"in mydict:
    print("publisher is one of the keys")
    #dictionaries can hold diff data types
mydict={
    "book":"dynamics",
    "publishers":"longhorn",
    "year":2001
    (["authors"]) ({"mike"})
}