'''
1.	With either one class or more than one class applied in inheritance , write a program that requests user 
to enter the value of length and width and then through the concept of method overloading, 
which have a method called rect() with different parameters do the following.
a)	Display such dimensions of a rectangle.        
b)	Determine the area of a rectangle.            
c)	Determine the perimeter of a rectangle. 	      

'''

class Dimensions:
    def __init__(self,l,w):
        self.l=l
        self.w=w
        
    def rect(self,l=None,w=None):
        if l is not None and w is not None:
           print(f"the length is {l} and the width is {w}")

        elif l is not None:
            return l*self.w
        
        else:
            return 2*(self.l + self.w)

Hei=int(input("enter the lenght::"))
wid=int(input("eneter the width::"))       
        
obj=Dimensions(Hei,wid)

obj.rect(Hei,wid)

print("the area is ",obj.rect(Hei) ," and the perimeter is", obj.rect())