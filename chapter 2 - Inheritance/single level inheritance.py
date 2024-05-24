class A:
    def feature1(self):
        print("this is feature1 ")
        
    def feature2(self):
        print("this is feature 2")
        
        
class B(A):# this is a child class of class A
    def feature3(self) :
        print("this feature 3")



 
obj=B()   

obj.feature1()