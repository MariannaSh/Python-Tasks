def f(n):
    n=str(n)
    a=[]
    for i in n:
        if int(i)%2!=0:
            a.append(int(i))
    if len(a)==0:
        return -1
    return max(a)-min(a)

print(f(10852))
print(f(7235973))
print(f(4388))
print(f(846206))


