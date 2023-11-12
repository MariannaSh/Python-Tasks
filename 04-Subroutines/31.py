def f(x,y):
    k=0
    for i in range(x,y-y):
        if i%2==0:
            k+=1
    return k

print(f(-7,8))
print(f(-1,11))

