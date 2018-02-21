def outside():
    x = 5

    def inside():
        print(x)

    return inside


myfun = outside()
myfun()

