class Rectangle:
    def rectangle(self,sideA,sideB):
        self.sideA=sideA
        self.sideB=sideB
        return sideA * sideB
    
    def mzingo(self,x,y):
        return 2*(x+y)


width=int(input("enter the width::"))
length=int(input("enter the length::"))

area=Rectangle()

print("the area of the rectangle is :: ",area.rectangle(width,length), "square unit of lenght")
   
    