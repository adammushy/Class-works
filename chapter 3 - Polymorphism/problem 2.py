'''
2.	Write a program that request user to enter three numbers, which must be passed in a class having a method called sum. 
The method must find the sum of the first two entered numbers and also find the sum of all entered numbers. 
Then create a child class which inherits both two sum methods but have method to display those two inherited methods.
'''

class Calc:  
    def __init__(self, x, y, z):
        self.x, self.y, self.z= x, y, z      
    def sum(self, x=None, y=None, z=None):
        if z is not None:
            return x + y + z
        else:
             return x + y
    
class Result(Calc):
    
        
    def display(self):
        print("the sum of first twon number is ",self.sum(self.x, self.y),"the sume of all 3 number is  ",self.sum(self.x, self.y, self.z))
        
        
   
a=int(input("enter 1st num::"))
b=int(input("enter 2nd num::"))
c=int(input("enter 3rd num::")) 

obj=Result(a, b, c)


obj.display()