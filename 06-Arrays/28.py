def f(arra1,arra2):  
    if len(arra1)==len(arra2):
        for i in range(len(arra1)):
            if arra1[i]==arra2[i]:
                return 'arrays are the same'
    return False
    
print(f(['water','book','sky'],['water','book','sky']))
print(f([True,False],[True,False,True]))
print(f([5,3,1],[5,3,1]))
print(f([3,2,1], [3,2]))
