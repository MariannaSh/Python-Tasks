# перевести число с деятичной системы в бинарную

def decimal_to_binary(decimal):
    binary = ''
    
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        binary += str(remainder)
    
    return binary[::-1]

print(decimal_to_binary(12))

def f(n):
    new=''
    
    while n>0:
        i=n%2
        n=n//2
        new+=str(i)
    return new[::-1]
print(f(12))
