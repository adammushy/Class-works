'''
8.	Write a python parent class called AreaPolygon having properties length, width, radius, base and height entered by the user.
Create a child class called Square which determine the area of the square with a method called area(). 
Create another subclass called Rectangle which inherits from the previous class but have the same method in this case 
it finds the area of a rectangle. Create another subclass called Triangle which inherits from the previous class 
but have the same method to find in this case the area of a triangle. Lastly create a class known as Circle which inherits 
from the Triangle have the same area method but in this case it finds the area of a circle. Create object(s) of class(es) which will help you to
access all the properties and behaviors defined/declared in the different scenarios of the  related classes and then print out the result. 
Is your application rely on overriding or overloading technique discuss?
'''


class AreaPolygon:
    l=int(input("enter the length::"))
    w=int(input("enter the width::"))
    r=int(input("enter the radius::"))
    h=int(input("enter the height::"))
    b=int(input("enter the base::"))
    
    

class Square(AreaPolygon):
    def area(self):
        return f"of Square: {self.l*self.l}"
    
    
class Rectangle(Square):
    def area(self):
        return  f"of Rectangle: {self.l * self.w}"


class Triangle(Rectangle):
    def area(self):
        return f"of Triangle: {0.5 * self.b * self.h}"    


class Circle(Triangle):
    def area(self):
        return f"of Circle: {3.14 * 0.25* self.r * self.r}"
    

square_obj = Square()
rect_obj = Rectangle()
tri_obj = Triangle()
circle_obj = Circle()


for x in (square_obj, rect_obj, tri_obj, circle_obj):
    print(">> Area",x.area())

"""
    The applications is based on overriding technique, because the area method in the child class, will override the super area method inherited
    from the parent class.
"""
 
 