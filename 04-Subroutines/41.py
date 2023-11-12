# def f(n):
#     new=[1]
#     for i in range(2,100):
#         k=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 k+=1
#         if k==2:
#             new.append(i)
#     return new[n]

# print(f(5))
# print(f(1))


def f(n):
    new=[1]
    for i in range(2,1000):
        k=0
        for j in range(1,i+1):
            if i%j==0:
                k+=1
        if k==2:
            new.append(i)
    return new[n]

print(f(1))
print(f(5))

