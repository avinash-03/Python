class Calculator:
    def __init__(self,num):
        self.number=num
    
    def square(self):
        print(f'the value of {self.number} square is {self.number**2}')
        pass

    def squareRoot(self):
        print(f"the value of {self.number} squareroot is {self.number**0.5}")
        pass

    def cube(self):
        print(f"the value of {self.number} cube is {self.number**3}")

    @staticmethod
    def greet():
        print("****hello there welcome to the best calculator****")
        


a=Calculator(9)
a.greet()
a.square()
a.squareRoot()
a.cube()