class Sum:
    def sum(self,a,b):
        return a + b # doing this show a , b bellongs to  class
    #if take  a,b  they belong to the method def 
    

num1=int(input("enter the num1::"))
num2=int(input("enter the num2::"))

obj=Sum()


print("the sum of the two numbers is ::",obj.sum(num1,num2))