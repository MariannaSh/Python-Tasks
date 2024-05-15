def f(arr):
    if len(arr)<3:
        return False
    for i in range(len(arr)):
       if arr.count(arr[i])==1:
           return arr[i]
    
print(f([7,7,5,7,7]))
print(f([4,3,4,4,4,4]))