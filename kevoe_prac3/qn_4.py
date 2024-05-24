class Sum:
    def __init__(self, a, b, w1, w2):
        self.a, self.b, self.w1, self.w2 = a, b, w1, w2
        
    def add(self):
        return self.a + self.b
    
    def word(self):
        return self.w1 + self.w2
    

class Product(Sum):
    def mult(self):
        return self.a * self.b
    
    def repstring(self):
        return self.w1 * 5


num1 = 5
num2 = 24

word1="BA"
word2="MA"

obj = Product(num1, num2, word1, word2)


print(">> The sum is ",obj.add(),"while the concatenation of the string is",obj.word(),
      "\n   The product is ",obj.mult(),"and the repetion of the string is ",obj.repstring())