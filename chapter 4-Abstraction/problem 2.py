'''
2.	Consider a class called Animal, this has got sub subclasses such as Tiger, Cow, HumanBeing, and Anaconda. 
The Animal class has a defined method known as eat, which is implemented in each and every subclass declared. 
Write a program to output what each class does, regarding that Tiger eats non vegetable, Cow eats vegetable, 
HumanBeing eats non vegetable and vegetable type of food while Anaconda enjoys swallowing other animals stuffs.
'''

from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):    
        pass

class Tiger(Animal):
    def eat(self):    
        print("the Tiger feed on Non vegetable food")

class Cow():
    def eat(self):    
        print("Cow feed on vegetable food")
        

class Human():
    def eat(self):    
        print("Human feed on both Non vegetable and vegetable food")
        
    
class Anaconda():
    def eat(self):    
        print("Anaconda enjoy swallowing ther animals and stuff")
        
    
    
tig=Tiger()
cow=Cow()
hum=Human()
anac=Anaconda()

tig.eat()
cow.eat()
hum.eat()
anac.eat()


