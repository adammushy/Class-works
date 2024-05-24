'''
6.	Write a program which will overload the area method. Regarding that if there is no argument then it returns 0. 
And if there is one argument then it returns the square of the value and assumes you are computing the area of a square. 
Also, if there will be two arguments then it returns the product of the two values and assumes you are computing the area of a rectangle.
'''


from turtle import width


class Rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self,l=None,w=None):
        if l == None and w==None:
            return 0
        
        elif l is not None and w is not None:
            return l*w
        
        else:
            if l is not None:
                return self.l * self.l
            else:
                return self.w* self.w
        
        
length=int(input("enter value::"))
width=int(input("enter value::"))

obj=Rectangle(length,width)

print(obj.area())
print("The area of the rectange is ",obj.area(length,width))
print("the square of each is",obj.area(None,width),obj.area(length))
        