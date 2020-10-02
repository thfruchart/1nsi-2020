# Chap4 EXO3

def max2(x,y):
    if x>y:
        return x
    else :
        return y

# autre solution
def max2(x,y):
    if x>y:
        return x
    return y

def max3(x,y,z):
    a = max2(x,y)
    b = max2(a,z)
    return b

# autre solution
def max3(x,y,z):
    return max2(max2(x,y),z)