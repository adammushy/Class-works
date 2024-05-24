from math import pi

class Circle:
    def  __init__ (self,r):#constructor
        self.r=r
    
    
    def area(self):
        return pi*self.r*self.r
    
    def perimeter(self):
        return 2 * pi * self.r
    
radius=int(input("enter the radius:: "))

obj=Circle(radius)#constructor

print("the area of the circle is",obj.area())

print("\n the perimeter of the circle is ::", obj.perimeter())