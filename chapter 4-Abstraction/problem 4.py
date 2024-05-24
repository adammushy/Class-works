'''
4.	Mileage  is the age of distance travelled in mile by a certain car from one place to another. Imagine you have different cars
travels from Morogoro to Dar such as Tesla has to travel by 30kmph, Suzuki has to travel 25kmph, Duster has to travel 24kmph 
and Renault has to travel 27kmph. Write python Abstraction with a class Car and abstract method mileage which 
will be implemented in subclasses those different cars. Output the mileage of each and every car declared.
'''

from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass
    
class Tesla(Car):
    def mileage(self):
        a="30km/h"
        print('the mileage of Tesla from moro to dar is',a)
    
class Suzuki(Car):
    def mileage(self):
        a="25km/h"
        print('the mileage of Suzuki from moro to dar is',a)
    
class Duster(Car):
    def mileage(self):
        a="24km/h"
        print('the mileage of Duster from moro to dar is',a)
    
class Renault(Car):
    def mileage(self):
        a="27km/h"
        
        
        print('the mileage of Renault from moro to dar is',a)
        
ob1=Tesla()
ob2=Suzuki()
ob3=Duster()
ob4=Renault()

ob1.mileage()
ob2.mileage()
ob3.mileage()
ob4.mileage()
