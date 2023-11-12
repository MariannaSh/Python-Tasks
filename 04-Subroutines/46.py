def f(x,y):
    summa=0
    for i in range(x,y+1):
        if i%2==0 and i%3==0 and i%4!=0:
            summa+=i
    return summa

print(f(1,20))
print(f(10,30))