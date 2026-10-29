def modify(string):
    if string.endswith("ing"):
        return string[:-3]+"ly"
    return string +"ing"
string=input("Enter the string:")
print(modify(string))