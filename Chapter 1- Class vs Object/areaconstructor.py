class Rectangle:
    def __init__ (self,a,b):
        self.a=a
        self.b=b
    
    
    def area(self):
        return self.a * self.b
    
    def perimeter(self):
        return 2 * (self.a + self.b)
    
    
    
length=int(input("enter the length::"))
width=int(input("enter width:: "))

mastra=Rectangle(length,width)


print("the area is ",mastra.area(), " and the perimeter is ",mastra.perimeter())
