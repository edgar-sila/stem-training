class Person:
    def __init__(self,name,dob,weight,height):
        self.name=name
        self.dob=dob
        self.weight=weight
        self.height=height
    def date_of_birth(self):
        dob=self.dob
        print(dob)
    def age(self):
        self.year=2004
        age =self.year-self.dob
        print(age)
    def weight(self):
        print(self.weight)
    def height(self):
        print(self.height)
    def bmi(self):
        bmi=(self.weight/{self.height**2})
        print(bmi)

class Student(Person):
    def _init__(self,name,dob,weight,height,class_studying,favourite_subject):
        super().__init__(name,dob,weight,height)
        self.class_studying=class_studying
        self.favourite_subject=favourite_subject
    def class_studying( self):
        print(self.class_studying)
    def favourite_subject(self):
        print(self.favourite_subject)

class Teacher(Person):
    def __init__(self,name,dob,weight,height,class_teaching,salary):
        super().__init__(name,dob,weight,height,class_teaching,salary)
        self.class_teaching=class_teaching
        self.salary=salary
    def class_teaching(self):
        print(self.class_teaching)
    def salary(self):
        print(self.salary)
# initials
a= Person  =("mishael",2004,58,170)
b= Student =("robinson",2003,57,153,"4w","chem")
c= Teacher =("lydia",1998,67,170,"4w",30000 ,"chem")

