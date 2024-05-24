'''
4.	By using operator overloading, create a class to add two numbers entered by user and have another method to overload 
the operator (+) by concatenating two strings (i.e BA and MA) entered by the user not only that but also 
create another class to print the product of the two numbers and have another method to repeat the String (BA) 
a number of times as you like (for a example 5 times). 
The output should be :-
The sum of the two numbers is  29  while concatenation of the strings is  BAMA 
And the product of the numbers is  120 
and fifth repetition of the word is  BABABABABA

'''
class Sum:
    def add(self,a,b):
        return a+b
    
    def word(self,x,y):
        return x+y
    

class Prod:
    def mult(self,a1,b1):
        return a1*b1
    
    def repstring(self,x1):
        return x1 * 5


num1=5
num2=24

word1="BA"
word2="MA"

obj1=Sum()
obj2=Prod()

print("the sum is ",obj1.add(num1, num2),"while the concatenation of the string is",obj1.word(word1,word2),
      "\n and the product is ",obj2.mult(num1, num2),"and the repetion of the string is ",obj2.repstring(word1))