class MyName:
    def __init__(self,l,w):
        self.l=l
        self.w=w
        
    def rect(self,l=None,w=None):
        if l ==None and w==None:
            print("the length is ",self.l, " and the width is ",self.w)
        elif l !=None: 
            return l*self.w
        else: 
            return 2*(self.l+self.w)
        
wi=int(input("enter the width::"))
leng=int(input("Enter the length::"))

obj=MyName(wi,leng)
obj.rect()

print("the area is ",obj.rect(wi) ," and the perimeter is", obj.rect(leng, wi))

        
            