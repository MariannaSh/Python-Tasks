arra1=[4,36,12,28,9,44,5]
arra2=[5,1,36]

for i in range(len(arra2)):
    if arra2[i] not in arra1:
        arra1.append(arra2[i])
print(arra1)