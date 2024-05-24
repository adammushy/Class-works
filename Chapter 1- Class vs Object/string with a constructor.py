from os import name


class Mjr:

    def __init__(self,name):
        self.name=name
        
        
    def get_string(self):
      return name
        
    def print_string(self):
        return self.name.upper()

user=input("enter value::")  
jina=Mjr(user)
x=jina.get_string()


print("UR NAME IS ::",jina.print_string())