 #it means 1 thing can take many forms
 #polymorphism is one of the OOPs feature that allows us to perform a single action in different ways
'''
#mostly use this wheen 
    -loose Coupling
    -dependency injection
    _interface
    
    
    
 Ways to implement
    1.duck typing
    2.Operator overloading
    3.method overloading
    4.method overriding
       
''' 

#DUCK TYPING

class PyCharm:
    def execute(self):
        print("Compiling")
        print("running")
        
        
class MyEditor:
    def execute(self):
        print("Cspell chek")
        print("code check")
        print("Compiling")
        print("running")



class Laptop:
    def code(self,ide):
        ide.execute()

ide=PyCharm()
ide=MyEditor()        
mastra=Laptop()



mastra.code(ide)