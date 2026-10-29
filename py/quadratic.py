import math
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=int(input("Enter the number:"))

q=(b*b) - 4*a*c
if q==0:
    x=-b/(2*a)
    print("The root is:",x)
elif q>0:
    x1=(-b+ (math.sqrt(b**2)-4*a*c))/(2*a)
    x2= (-b - (math.sqrt(b ** 2) - 4 * a * c)) / (2 * a)
    print("The roots are:",x1,x2)
else:
    print("No roots")
