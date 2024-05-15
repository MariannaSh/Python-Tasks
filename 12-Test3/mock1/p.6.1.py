def f(name):
    if not (1 <= len(name) <= 5):
        return False
    if not (name[0].isalpha() or name[0] == '_'): # first character check
        return False
    for i in range(1, len(name)):
        if not (name[i].isalnum() or name[i] == '_'): #проверка оставшихся символов
            return False
    return True

print(f('abc'))
print(f('abcdses'))
print(f('Abc'))
print(f("_ab_c"))