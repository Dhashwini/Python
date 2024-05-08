class Calculator:
    def __init__(self,a,b):
        self.num1 = a
        self.num2 = b
    def add(self):
        print("Enter adddition of two values:",self.num1+self.num2)
    def sub(self):
        print("Enter subraction of two values:",self.num1-self.num2)
    def mul(self):
        print("Enter multiplication of two values:",self.num1*self.num2)
    def div(self):
        print("Enter divison of two values:",self.num1/self.num2)
    

        
res = Calculator(16,8)
res.add()
res.sub()
res.mul()
res.div()

 
