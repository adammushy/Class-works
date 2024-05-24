#Encapsulation  is a process of wrapping code and data together into a single unit.

from pickle import OBJ


class Add:
    __a, b = 5, 10
    
    def sum(self):
        return self.__a + self.b

        
class Add1(Add):
    def display(self):
        print(f">>The sum is {self.sum()} ")
        #print(f"Trying {self.__a + self.b} ")
    
        
        
obj = Add1()
obj.display()
 
 