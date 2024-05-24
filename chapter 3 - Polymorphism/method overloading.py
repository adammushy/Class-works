class Car:
    def wheels(self):
        print("the are four(4) wheels")
        
    def  transport(self):
        print("private Transport")
        
        
        
class Bus:
    def wheels(self):
        print("the are Eight(8) wheels")
        
    def  transport(self):
        print("public Transport")
        
        
obj1=Car()

obj2=Bus()

for x in (obj1,obj2):
    x.wheels()
    x.transport()