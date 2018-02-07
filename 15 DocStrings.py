# 15. DocStrings
def print_alpha():
    '''this function is used print alphabet'''
    alpha = [chr(i) for i in range(65, 91)]
    print(alpha)
print(print_alpha.__doc__)
print_alpha()