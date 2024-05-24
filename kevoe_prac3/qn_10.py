class Numbers:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def prod(self,a=None,b=None):
        if a == None and b==None:
            return print('No values entered')
        
        elif a is not None and b is not None:
            return print(f">> Sum: {a + b} ")
        
        elif a is not None and b is None:
            return print(f">> Product: {a * a}")
           
        else:
            return print(f"Product: {b* b}")
            
num1 = int(input("Enter the first value: "))
num2 = int(input("enter the second value: "))

obj = Numbers(num1,num2)


obj.prod()
obj.prod(num1,num2)
obj.prod(num1)
obj.prod(num2)