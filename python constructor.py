class Man:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('my name is', self.name)


p = Man('Amit')
p.say_hi()

