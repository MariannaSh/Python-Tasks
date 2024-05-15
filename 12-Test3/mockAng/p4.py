def f(vname):
    if len(vname)==0 or len(vname)>6:
        return False
    if 0<len(vname)<5:
        for i in range(len(vname)):
            if vname[0].isalpha() or vname[0]=='_':
                if not (vname[i].isalpha() or vname[i].isdigit() or vname[i]=="_"):
                    return True
        return False

print(f('abc'))
print(f('abcdses'))
print(f('Abc'))
print(f("_ab_c"))

# v='_b45d'
# print(v[1::])
# for i in range(len(v)):
#     if v[0].isalpha() or v[0].isupper() or v[0]=='_':
#         print(True)