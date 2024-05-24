#abstract method is the method which has got declaation but has got no definition
#and the class wich has abstract method is called abstract class  
#an abstract class need to have atleast 1 abstract method
#for python you have to import a module since it doesnot support it by default
#for examople of abstact class and methoid



#Abstraction is a technique of hiding unnecessary details from the user. 

'''
class abstract :
    def methdabstract(self):
        pass #this show that the methdo hasnot been defined but has been declared
        

'''
from abc import ABC,abstractmethod



class One(ABC):
    @abstractmethod #this is a decorator showing that this is an anbstract class 
    def  mastra(self):
        pass

class Two(One):
    def mastra(self):
        print("running")
         
class Mushi():
    def mastra(self):
        print("welcome")    
        
class Three:
    def three(self,com,com1):
        com.mastra()
        com1.mastra()
        print("compliting")


obj1=Two()
obj2=Mushi()
#obj1.mastra()

tre=Three()
tre.three(obj2,obj1)