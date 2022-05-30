


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def details(self):
        print(f"my name is {self.name} and my age is{self.age}")

p1= Person ("sebastian",19)
p1.details()




class Employee(Person):
    def __init__(self,name,age,salary):    
        super().__init__ (name ,age)
        self.salary = salary
p2 =Employee("sebastian",19,5000)
p2.details()
def details(self):
        print(f"my name is{self.name}and my age is{self.age}and i earn asalary of{self.salary}")
def birthday(self):
        self.age=self.age+1
        print(f"happy birthday,you are now{self.age}years old")