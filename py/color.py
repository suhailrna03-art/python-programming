
cl1=["orange","green","red"]
print("cl1=",cl1[-1])

cl2=["orange","blue","brown","red"]
d=[color for color in cl1 if color not in cl2]
print("difference=",d)