# so as to perform overriding there should be inheritance
class StudentAge:
    name=input("enter name::")
    age=input("enter your age::")
    
    def info(self):
        print("Your name is ",self.name," your age is ",self.age)
        
class Student(StudentAge):
    name=input("enter name::")
    age=input("enter your age::")
    
    def info(self, o=False):
        if o == True:
            print(f"{super().name} is {super().age}")
            print("While ",self.name," age is ",self.age)
            return
        
        print("Your name is ",self.name," your age is ",self.age)
        return
    
            
        


obj = Student()


obj.info()



print("\nIn avoiding method overriding the method must implement overloading\n")

obj.info(o=True)