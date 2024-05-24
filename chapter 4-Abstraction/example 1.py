from abc import ABC, abstractmethod

class Add(ABC):
    x=5
    y=4
    
    @abstractmethod
    def sum(self):
        pass
    
class Add1(Add):
    def sum(self):
        print("the sum of the two num is ",self.x + self.y)
         
obj=Add()
obj.sum()


