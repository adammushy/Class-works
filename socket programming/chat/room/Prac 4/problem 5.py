'''
5.	Write a python abstract by declaring an abstract class called Polygon having abstract method sides which must implemented in Triangle,
Pentagon,Hexagon and Square. Regarding that Triangle  should implement the method by outputting “Triangle has 3 sides”, 
while Pentagon outputting “Pentagon has 5 sides”, Hexagon outputting “Hexagon has 6 sides”, and Square outputting “I  have 4 sides”,

'''

from abc import ABC,abstractmethod

class Polygon(ABC):
    @abstractmethod
    def sides(self):
        pass

class Triangle(Polygon):
    def sides(self):
        print('triangle has three sides')
        
class Pentagon(Polygon):
    def sides(self):
        print('pentagon has three sides')
        
class Hexagon(Polygon):
    def sides(self):
        print('hexagon has three sides')

class Squire(Polygon):
    def sides(self):
        print('Squire has three sides')
        
ob1=Triangle()
ob2=Pentagon()
ob3=Hexagon()
ob4=Squire()

ob1.sides()
ob2.sides()
ob3.sides()
ob4.sides()