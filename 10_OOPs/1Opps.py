class Number:
    def sum(self):
        return self.a + self.b

num=Number()
num.a=3
num.b=4

print(num.sum())

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
