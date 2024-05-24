class A:
    def __init__(self) :
        print("this is A init")
    
    def feature1(self):
            print("this is feature one")
        
    def feature2(self):
        print("this is feature two")


class B:
    def __init__(self):
        super().__init__()
        print("this is B init")        

    def feature3(self):
            print("this is feature three")
        
    def feature4(self):
        print("this is feature four")

class C (A,B):
    
    def __init__(self):
        super().__init__()
        
        print("this is C init")
    
    def feat(self):
        super().feature2()
        
        
        
mastra=C()
mastra.feat()



