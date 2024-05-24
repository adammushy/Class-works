'''
3.Consider a class called StudentAge, this have properties name and age and have method to display the name and age entered in the system.
A subclass is to be created having all properties and behavior from the StudentAge but have it’s own name and age and the same method and
same parameter as that one of StudentAge. Write a program to show how StudentAge is overridden by the subclass method declared. 
How do you do if you want to avoid override method?, for a instance the output be :-

John Edward 25 years
While Win James 23 years

'''
# so as to perform overriding there should be inheritance

class StudentAge:
    name=input("enter name::")
    age=input("enter your age::")
    
    def info(self):
        print("Your name is ",self.name," your age is ",self.age)
        

class Student(StudentAge):
    name=input("enter name::")
    age=input("enter your age::")
    
    def info(self):
        print("Your name is ",self.name," your age is ",self.age)
        

obj1=StudentAge()
obj=Student()


obj.info()

print("\nto avoid method overriding let do method overloading\n")

# to avoid method overriding let do method overloading

for child in (obj,obj1):
    child.info()