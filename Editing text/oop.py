from zmq import DEALER


class Dog:
    def __init__(self,no_of_eyes,colour,no_of_legs):
        
        self.no_of_eyes=no_of_eyes
        self.colour=colour
        self.no_of_legs=no_of_legs
    def bark(self):
        print('woof woof!')    
        
spitz=Dog(no_of_eyes=2, colour="white",no_of_legs=4)
chihuahua=Dog(no_of_eyes=1,colour="black", no_of_legs=4)
dobberman=Dog(2,"brown",no_of_legs=4)
pormerian=Dog(no_of_legs=4,colour="black",no_of_eyes=2)

print(spitz.no_of_eyes,spitz.no_of_legs,spitz.colour)
print(chihuahua.colour,chihuahua.no_of_eyes,chihuahua.no_of_legs)
print(dobberman.no_of_eyes)
print(pormerian.colour,pormerian.no_of_eyes,pormerian.no_of_legs)




spitz.colour="darkbrown"
print(spitz.colour)

print("woof woof!")
   
