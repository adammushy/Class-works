class AreaPolygon:
    l=int(input("enter the length::"))
    w=int(input("enter the width::"))
    r=int(input("enter the radius::"))
    h=int(input("enter the height::"))
    b=int(input("enter the base::"))
    
    

class Square(AreaPolygon):
    def area(self):
        return self.l*self.l
    
    
class Rectangle(Square):
    def area(self):
        return  self.l * self.w


class Triangle(Rectangle):
    def area(self):
        return 0.5 * self.b * self.h    


class Circle(Triangle):
    def area(self):
        return 3.14 * 0.25 * self.r * self.r
    

obj_square = Square()
obj_rect = Rectangle()
obj_tri = Triangle()
obj_circle = Circle()


for x in (obj_square,obj_rect,obj_tri,obj_circle):
    print("the area is :",x.area())

 