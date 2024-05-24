'''
3.	Write a python parent class called AreaPolygon having properties length, width, radius, base and height entered by the user
and have defined method area. Create a child class called Square which determine the area of the square. 
Create another subclass called Rectangle which inherits from the parent class but in this case it finds the area of a rectangle. 
Create another subclass called Triangle which inherits from the base class but have the same method to find the area of a triangle. 
Lastly create a class known as Circle which inherits from the super class but have the same method but in this case it finds the area of a circle. 
Create object(s) of class(es) which will help you to access all the properties and behaviors defined/declared 
in the different scenarios of the related classes and then print out the result.
'''
from abc import ABC,abstractmethod
from math import pi


class AreaPolygon(ABC):
    l=int(input("enter the length::"))
    w=int(input("enter the width::"))
    r=int(input("enter the radius::"))
    h=int(input("enter the height::"))
    b=int(input("enter the base::"))
    @abstractmethod
    def Area(self):
        pass
    
class Square(AreaPolygon):
    def Area(self):
        area=self.l*self.l
        print("the area of square is ",area)
        
    

class Rectangle(AreaPolygon):
    def Area(self):
        area=self.l*self.w
        print("the area of rectangle is ",area)

class Triangle(AreaPolygon):
    def Area(self):    
        area=0.5*self.h*self.b
        print("the area of triangle is ",area)
    

class Circle(AreaPolygon):
    def Area(self):
        area= pi*self.r*self.r
        print("the area of circle is ",area)

obj_square=Square()
obj_rect=Rectangle()
obj_tri=Triangle()
obj_circle=Circle()

for x in (obj_square,obj_rect,obj_tri,obj_circle):
    x.Area()