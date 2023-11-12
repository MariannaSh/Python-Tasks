
def f(product_code):
    sum=int(product_code[0])+int(product_code[1])+int(product_code[2])
    if sum%7 != int(product_code[-1]):
        return False
    return True

print(f('1082'))
print(f('2035'))
print(f('1114'))
print(f('7071'))    