n=int(input("Enter the year:"))
if n% 400==0 or (n% 4==0 and n% 100!=0):
    print("This is a leap year",n)
else:
    print("it is not a leap year",n)