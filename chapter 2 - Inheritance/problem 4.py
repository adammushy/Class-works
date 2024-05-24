class Dit:
    full_name=input("enter your full name:: ")
    Regno=int(input("enter your regno:: "))

class CSdepartment(Dit):
    def details(self):
        print("my full name is",self.full_name.upper()," with registration number ",self.Regno ) 
    
    
obj=CSdepartment()
obj.details() 