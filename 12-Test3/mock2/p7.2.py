def f(d):
    new=[]
    for k,v in d:
        if v=='in':
            new.append(k)
        if v=='out':
            new.remove(k)
    return sorted(new)


cars=[["KR234","in"],["BA123","in"],["GX444","in"],
      ["KR234","out"], ["BA111","in"],["BA123","out"],["KR234","in"]]
print(f(cars))

cars1 = [["KR234","in"],["KR234","out"]]
print(f(cars1))
