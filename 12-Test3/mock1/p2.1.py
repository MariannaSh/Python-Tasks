def f(x,y,digit):
    count=0
    for i in range(x,y+1):
        for j in range(len(str(i))):
           if str(digit) in str(i)[j]:
               count+=1
    return count

print(f(10,15,1))
print(f(28,32,2))
print(f(100,105,6))
print(f(100,101,0))
        