from email import message
from re import S

from pkg_resources import safe_name


name="Edgar sila"

#Multiple line strings
message='''QWERTYTTT MPESA YOU HAVE RECIEVED 2000 FROM EDGAR'''
print (message)

city="nairobi"
#.upper()to convert to upper case
print(city.upper())

uni="JKUAT"
print(uni.lower())
fruit="grapes"
print(fruit[:2])
print(fruit[:5])
print(fruit[:-1])

#strip removes spaces between word
f_name="e_d_g_a_r"
print(f_name.strip())
s_name = "owino"
fullname = f_name+s_name

print(fullname)

city="mombasa"

print(len(city))

#int ->string
x=3.14 #float
z=1
print(str(x))
