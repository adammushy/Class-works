
#7.	With example show that is it possible to override protected method as private?
'''
in python there is no private method that cannot be accessed inside a class
Though you can define a private method by using double underscore before the name of the method
EXAmple    

'''
class Parent:
        def society(self):# declaring public method
            print("this is public method")
            
        def __personal(self):
            print("this is private method")

#insted we can call the method inside another method in same class
        def call(self):
            self.__personal()
            
            
class Child(Parent):#this is a derived class(sub class)
    def call_public(self):# call public from class parent
        print("\nFrom the parent class")
        self.society()
    def __personal(self):
            print("this is private gang")

    
    def call_private(self):
        self.__personal()
                                
  
#obj1=Parent()
#obj1.society()
#obj1.__personal() calling this will rise attribute error
#obj1.call()

obj=Child()
obj.society()
#obj.__personal() also this rise an error
obj.call_private()
       