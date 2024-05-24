'''

9.	Write a program which asks user to enter a number of parameters when a method is called. This program should have a class 
which have a method to accept whether a number is passed, none of the numbers passed or accept two numbers from the user. 
The program should return the product of two numbers if it accepts two values, square of the number if it accepts any of the value
and return zero if it does not accept any value and then the program should output all the scenarios involved.

'''
from re import L


class Number:
    def __init__(self,l,w):
        self.l=l
        self.w=w
        
    def result(self,l=None,w=None): 
        if l is not None and w is not None:
            prod=self.l*self.w
            print(f"the product of the two number is",prod)
           

        elif l is not None and w is None:
            return l*l
        
        elif l is None and w is not None:
            return w*w    

        
        else:
            return 0
        

num1=int(input("enter num1::"))
num2=int(input("eneter num2::"))       
        
obj=Number(num1,num2)

obj.result(num1,num2)

print("the square of a single number is",obj.result(num1) ,"  or  ",obj.result(num2)," since both are none hence the result is", obj.result())