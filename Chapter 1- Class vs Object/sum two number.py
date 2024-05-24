#a=int(input("enter the num1::"))
#b=int(input("enter num2::"))

def sum(a,b):
    return a+b

num1=int(input("enter the num1::"))
num2=int(input("enter the num2::"))

#using eval instead of int it will consider input to it specific data types

print("the of the two numbers is:: ",sum(a=num1,b=num2))