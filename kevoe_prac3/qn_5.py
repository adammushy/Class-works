class Parent:
    def add(self,a,b):     
        self.a=a
        self.b=b
        return self.a + self.b
        
        
class Child:
    def add(self,a,b,c,):
        self.a=a
        self.b=b
        self.c=c
        return self.a+self.b+self.c
    
    
class  Display(Parent,Child):
    def result(self,a,b,c):
        print("parent is",Parent.add(self,a,b), "the child is ",Child.add(self,a,b,c))

num1=int(input("enter value::"))
num2=int(input("enter value::"))
num3=int(input("enter value::"))

obj=Display()

obj.result(num1,num2,num3)
