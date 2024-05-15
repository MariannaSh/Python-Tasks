def push(value):
    stack=''
    while value!=0: 
        stack+=str(value%2)
        value=value//2
    return stack[::-1]


print(push(18))
