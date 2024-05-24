from abc import ABC,abstractmethod
from unicodedata import name

class  Name():
    @abstractmethod
    def  name(self):
        pass
        #print('Hello')
    
class Name1(Name):
    jina="john Edward"
    def name(self):
        print("my name is ",self.jina) 
        

class Name2(Name):
    jina="Adam El Mastra"
    def name(self):
        super().name
        print("my name is ",self.jina)
        

obj=Name1()
obj1=Name2()

obj.name()
obj1.name()
               