def f(number,even):
    summa=0
    for i in str(number):
        if even==True:
            if int(i)%2==0:
                summa+=int(i)
        elif even == False:
            if int(i)%2!=0:
                summa+=int(i)
    return summa

# print(f(3124,True))
# print(f(3124,False))
# print(f(20576,False))
# print(f(20576,True))
# print(f(13115,True))
