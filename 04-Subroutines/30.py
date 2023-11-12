def f(number,even):
    summa=0
    number=str(number)
    if even == True:
        for i in number:
            if int(i)%2==0:
                summa+=int(i)
    elif even == False:
        for i in number:
            if int(i)%2!=0:
                summa+=int(i)
    return summa

print(f(3124,True))
print(f(3124,False))
