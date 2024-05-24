class Number:
    def __init__(self,l,w):
        self.l=l
        self.w=w
        
    def result(self,l=None,w=None): 
        if l is not None and w is not None:
            prod=self.l*self.w
            print(f"the product of the two number is",prod)
           

        elif l is not None and w is None:
            return l*l
        
        elif l is None and w is not None:
            return w*w    

        
        else:
            return 0
        

num1 = int(input("enter num1::"))
num2 = int(input("eneter num2::"))       
        
obj=Number(num1,num2)

obj.result(num1,num2)

print("the square of a single number is",obj.result(num1) ,"  or  ",obj.result(num2)," since both are none hence the result is", obj.result())
 