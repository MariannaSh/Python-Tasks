def f(product_code):
    sum=0
    if 0<(len(product_code))<=3 or (len(product_code))>4:
        return False
    if (len(product_code))==4:
        for i in range(len(product_code)-1):
            sum+=int(product_code[i])
        if sum%7!=int(product_code[-1]):
            return False
    return True

print(f('1082'))
print(f("2035"))
print(f("498384"))
print(f("704"))


# f='1114'
# sum=0
# for i in range(len(f)-1):
#     sum+=int(f[i])
# if sum%7==int(f[-1]):
#     print(True)