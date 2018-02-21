def addOne(myFunc):
    def addOneInside():
        return myFunc() + 1
    return addOneInside


def oldFunc():
    return 5;


newFunc = addOne(oldFunc)
print(oldFunc(), newFunc())

