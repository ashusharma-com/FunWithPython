class test:

    def product(self, a, b, c):
        p = a * b * c
        print(p)

    def product(self, a, b):
        p = a * b
        print(p)


t = test()
try:
    t.product(4, 5)
    t.product(4, 5, 5)
except Exception as err:
    print("method overloading not possible", err)