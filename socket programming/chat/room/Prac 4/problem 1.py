'''
1.	Write a python abstraction to examine the class Shape and its subclasses Rectangle and Circle defined in the script shape. 
Each of the subclasses Rectangle and Circle needs methods for computing area and perimeter. 
Then output the area and perimeter defined in each subclass when user has to enter values length, width and radius.
'''
from abc import ABC,abstractmethod
from math import pi
class Shape(ABC):
    l=int(input("enter the length::"))
    w=int(input("enter width::"))
    r=int(input("enter radii::"))
    @abstractmethod
    def area(self):
        pass
    @abstractmethod  
    def perimeter(self): 
        pass

class Rectangle(Shape):
    def area(self):
        return self.l*self.w

    def perimeter(self):
        return 2*(self.l+self.w)
    
        
class Circle(Shape):
    def area(self):
        return pi*self.r*self.r
    
    def perimeter(self):
        return 2*pi*self.r
    

circ=Circle()
rect=Rectangle()

for x in (circ,rect):
    print("the area is ",x.area())
    print("the perimeter ",x.perimeter())
