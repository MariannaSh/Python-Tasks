
def f(uid):
    return len(uid) == len(set(uid))
#функция set() преобразует список uid в набор уникальных элементов

print(f(["john5","ann123","JOHN5","xxx","abc333","a10"])) # True
print(f(["abc123","ann","abc123","a10"])) # False
print(f(["bob2","bob2"])) # False
print(f(["bob2","BOB2"])) # True