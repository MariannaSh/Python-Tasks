
# def f(password):
#     if len(password)<6:
#         return False
#     if len(password)>=6:
#         for i in password:
#             if password.count(i)>1:
#                 return False
#     return True
    
# print(f('ax12'))
# print(f('book123'))
# print(f('A2water3'))
# print(f("qwerty"))
# print(f(''))

def f(n):
    if len(n)<6:
        return False
    if len(n)>=6:
        for i in n:
            if n.count(i)>1:
                return False
        return True
    
print(f('ax12'))
print(f('book123'))
print(f('A2water3'))
print(f("qwerty"))
print(f(''))



# p4 print(f('abcbd')) => a+b-c+b-d

def f(n):
    n=list(n)
    for i in range(len(n)):
        if i%2==0:
            n[i]+='+'
        else:
            n[i]+='-'
    return ''.join(n)[:-1]

print(f('sds'))





