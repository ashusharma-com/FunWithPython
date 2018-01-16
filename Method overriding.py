class Base():

    def add(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        sum = a + b + c
        print(sum, " [ base class ]")


class Derived(Base):
    def add(self, a, b):
        sum = a + b
        print(sum, " [ derived class ]")


objOfBase = Base()
objOfDerived = Derived()

objOfBase.add(4, 2, 5)
objOfDerived.add(4, 2)
