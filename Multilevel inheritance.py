class Add:

    def add(self, num1=0, num2=0):
        total = num1 + num2
        print(num1, "+", num2, "=", total)


class Sub(Add):

    def sub(self, num1=0, num2=0):
        total = num1 - num2
        print(num1, "-", num2, "=", total)


class Mul(Sub):

    def mul(self, num1=0, num2=0):
        total = num1 * num2
        print(num1, "*", num2, "=", total)


obj = Mul()
obj.add(1, 2)
obj.sub(1, 2)
obj.mul(1, 2)
