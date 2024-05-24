class Calculation1:
    def sum(self,a,b):
        return a + b

class Calculation2:
    def multiplication(self,m,n):
        return m * n

class Calculation3(Calculation1,Calculation2):
    def division(self, x,y):
        return x/y


    
    
num1=int(input("enter the 1st number:: "))
num2=int(input("enter the 2nd number:: "))

obj=Calculation3()


print(obj.division(num1,num2))
print(obj.sum(num1,num2))

print(obj.multiplication(num1,num2))

