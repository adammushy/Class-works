class Rectangle:
    height=int(input("enter the height:: "))
    width=int(input("enter the width:: "))
    
    def display(self):
        print("your height is ",self.height,"and the width is ",self.width)
        
        
       
class RectArea(Rectangle):
    def Area(self):

      return self.height * self.width
     

class RectPer(Rectangle):
    def Perimeter(self):
       return 2 *(self.height + self.width)
        
class Display(RectArea,RectPer):
    def display(self):
        print("your area is ",self.Area() , " and the perimeter is ",self.Perimeter())
        
        
        
obj=Display()
obj.display()