def f(n):
    n=str(n)
    new=[]
    for i in n:
        if int(i)%2!=0:
            new.append(int(i))
    if len(new)==0:
        return -1
    return max(new)-min(new)


print(f(10852))
print(f(7235973))
print(f(4388))
print(f(846206))
