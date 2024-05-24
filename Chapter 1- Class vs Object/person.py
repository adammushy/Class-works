class Person:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
        
        
    def printname(self):#the difference between the method and function ,the method has (self) as default arg while function has ()
        return self.firstname + " " +self.lastname
    
    
name1=input("enter name::")
name2=input("enter name::")    
p1=Person(name1,name2)


print("your name is ::", p1.printname())