class Dimensions:
    def __init__(self, height, width) :
        self.height, self.width = height, width
        
    def rect(self, a=False, p=False, d=False):
        if d is True:
           print(f">> length = {height} \n   Width = {height}")

        elif a is True:
            return self.height * self.width
        
        else:
            return 2*(self.width + self.height)

height = int(input("Enter the length: "))
width = int(input("Enter the width: "))       
        
obj = Dimensions(height, width)

obj.rect(d=True)

print(">> The area is ",obj.rect(a=True) ," and the perimeter is", obj.rect(p=True))