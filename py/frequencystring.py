string=input("Enter the string:")
freq ={}
for ch in string:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print("Character string=",freq)
