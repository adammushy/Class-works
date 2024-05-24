class Fetch:      
                
    def get_string(self):
       return input("enter value::")
        
        
    
                
    def print_string(self,insert):
        self.insert=insert
        print(self.insert.upper())
        


obj=Fetch()
mastra=obj.get_string()
obj.print_string(mastra)




        