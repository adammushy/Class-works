class Dit:
    student=input("enter student name :: ")
    teacher=input("enter teacher name :: ")
    
    def printmethod(self):
        print("the student is ", self.student,"while the teacher is ", self.teacher)
        
    
    
    
class Department(Dit):
    module=input("enter the modyle name:: ")
    
    def modulename(self):
        print("the module is ", self.module)

obj=Department()
obj.printmethod()
obj.modulename()