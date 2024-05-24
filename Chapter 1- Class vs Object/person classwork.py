class Person:
    fname=input("enter firstname :: ")
    lname=input("enter lastname :: ")
    

    def printname(self):
        print("my name is ", self.fname ," ",self.lname )    
    
    
    
obj=Person()
obj.printname()