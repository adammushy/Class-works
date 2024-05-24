class TwoDShape:
    height=int(input("enter the height:: "))
    width=int(input("enter the width:: "))
    ShowDim=print(f"your height is {height} and width is {width}")
    
    
class Triangle(TwoDShape):
    def area(self): 
        return 0.5 * self.height *  self.width
    
    
class Result(Triangle):
    def answer(self):
        print ("area is " ,self.area())
        
    
obj=Result()
obj.answer()
