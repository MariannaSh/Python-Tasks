def f(arr2D):
    for i in arr2D:
        i[0],i[-1]=i[-1],i[0]
    return arr2D
    

print(f([[2,1],[3,4]]))

