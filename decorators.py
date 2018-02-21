def funOne(fun):
    def funTwo():
        return "Hello "+fun()
    return funTwo()

@funOne
def funThree():
    return "World"

print(funThree)
