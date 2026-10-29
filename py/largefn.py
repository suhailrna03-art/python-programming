def find_largest(a,b,c):
    """Returns the largest among three numbers"""
    if a>=b and a>=c:
        return a
    elif b>=a and b>c:
        return b
    else:
        return c
print(find_largest(100,70,120))