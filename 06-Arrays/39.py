array=[1,2,3,4,5,6,7]
even=[]
odd=[]
for i in array:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even+odd)