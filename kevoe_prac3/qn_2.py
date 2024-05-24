class Calc:        
    def sum(self, a=None, b=None, c=None):
        if c is not None:
            return a + b + c
       
        return a + b
    
class Result(Calc):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
        
    def display(self):
        print("the sum of first twon number is ",self.sum(self.a, self.b),"the sume of all 3 number is  ",self.sum(self.a, self.b, self.c))
        
        
   
a=int(input("enter 1st num::"))
b=int(input("enter 2nd num::"))
c=int(input("enter 3rd num::")) 

obj=Result(a, b, c)

obj.display()