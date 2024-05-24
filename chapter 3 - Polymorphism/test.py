class Parent():
    def add(self,a,b):
        self.a=a
        self.b=b
        return a+b
    
class Child():
    def add(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        return a+ b + c                

class Display(Parent,Child):
    def display(self,a,b,c):
        print("the sum of two num:: ",Parent.add(self,a,b),"and the sum of 3 num ::", Child.add(self,a,b,c))
        

num1=int(input("enter value::"))       
num2=int(input("enter value::"))  
num3=int(input("enter value::"))       
      
        
obj=Display()

obj.display(num1,num2,num3)