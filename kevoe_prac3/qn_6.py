
class Rectangle:
    def area(self, length=None, width=No.knxkjw2    ne):
        if length == None and width == None:
            return 0
        
        if length is not None and width is not None:
            return length * width
        
        if length is not None and width is  None:
            return length * length
        
        if length is None and width is not None:
            return width * width
           
        
        
length = int(input("enter value::"))
width = int(input("enter value::"))

obj=Rectangle()

print(obj.area())
print(">> Area of the rectange is ",obj.area(length,width))
print(f">> Square of each is {obj.area(None,width)} , {obj.area(length)}")
        