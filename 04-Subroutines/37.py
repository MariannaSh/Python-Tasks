# def f(n):
#     if n<=0:
#         return False
#     elif n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return f(n-1)+f(n-2)
 
# print(f(5))
# print(f(9))

# def f(n):
#     fibonacci=[0,1]
#     f=0
#     for i in range(2,100):
#         f=fibonacci[i-1]+fibonacci[i-2]
#         fibonacci.append(f)
#     return fibonacci[n-1]

# print(f(5))
# print(f(9))

def f(n):
    fibonacci=[0,1]
    f=0
    summa=0
    for i in range(2, n):
        f=fibonacci[i-1]+fibonacci[i-2]
        fibonacci.append(f)
    for k in fibonacci:
        summa+=k
    return summa

print(f(5))
print(f(9))

def f(n):
    fibonacci=[0,1]
    f=0
    for i in range(2,n+1):
        f=fibonacci[i-1]+fibonacci[i-2]
        fibonacci.append(f)
    return fibonacci[n-1]

print(f(5))