'''
10.	Write a program that request user to enter a number, two numbers, or three numbers which must be passed in a class having a method 
called sum and overload the method to perform all three different scenarios which must be printed on the screen.
'''

class Numbers:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def prod(self,a=None,b=None):
        if a == None and b==None:
            return 0
        
        elif a is not None and b is not None:
            return a+b 
        
        elif a is not None :
            return a*a
           
        else:
            return b* b
            
            
num1=int(input("enter the value::"))
num2=int(input("enter the value::"))

obj=Numbers(num1,num2)


print("if both are none return ",obj.prod()," if both are not none return sum is ",obj.prod(num1,num2),
      f" and if either of the two is nor return {obj.prod(num1)} if 'a' was none and return {obj.prod(num2)} if 'b' was none")