def f(arra1,arra2):
    for i in arra1:
        if i not in arra2:
            return False
    return True

print(f([3,6,2,1],[3,2,4,6]))
print(f([3,6,2,1],[3,2,1,6]))