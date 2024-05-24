class A:
    def feature1(self):
        print("this is feature one")
        
    def feature2(self):
        print("this is feature two")
    
    def feature1(self):
            print("this is feature one ")
        
    def feature2(self):
        print("this is feature two")
        
        
class B:
    
    def feature3(self):
            print("this is feature three ")
        
    def feature4(self):
        print("this is feature four")
        
        
class C(A,B):
 
    def feature5(self):
            print("this is feature five")
        
    def feature6(self):
        print("this is feature six") 
          
        
mastra=C()

mastra.feature2()  