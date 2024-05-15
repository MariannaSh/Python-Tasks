def f(d):
    
    summa=0
    count=0
    for key,value in d.items():
        summa+=value
    av=summa/len(d)
    for key,value in d.items():
        if value>av:
            count+=1
    return count

print(f({"LO231":150,"BA787":120,"NZ15":30}))
print(f({"LO231":150,"BA787":20,"NZ15":30}))