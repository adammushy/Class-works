from math import pi

class Area:
    def area(self,yo):
        self.yo=yo
        return pi * self.yo
    
    
    def perimeter(self, r):
        self.r=r
        return 2 * pi * self.r
    
num=int(input("enter your radius::"))    
num1=Area()

print("the area of the circle is ::", num1.area(num), "and the perimeter is ::", num1.perimeter(num))
