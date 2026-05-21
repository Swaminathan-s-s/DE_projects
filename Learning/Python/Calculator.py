class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        c = self.a + self.b
        print("The sum of a and b is:", c)
        return c

    def sub(self):
        c = self.a - self.b
        if self.a > self.b:
            print("the difference between a and b is:", c)
        else:
            print("a is lesser than b so ans will be negative")
            print("the difference between a and b is:", c)
        return c

    def mult(self):
        c = self.a * self.b
        print("the multiplied value of a and b is:", c)
        return c

    def div(self):
        if self.b != 0:
            c = self.a / self.b
            print("the quotient of a divided by b is:", c)
            return c
        else:
            print("Division by zero")
            return None
        
if __name__ == "__main__":
    a = int(input("Enter the value for a: "))
    b = int(input("Enter the value for b: "))

    calc = Calculator(a, b)
    calc.add()
    calc.sub()
    calc.mult()
    calc.div()