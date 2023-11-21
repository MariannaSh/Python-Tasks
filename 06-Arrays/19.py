import random 

arr1 = [3,7,1,0,4]
print(f'a)', arr1)
arr2 = [[2,3],[7,1],[0,4]]
print(f'b)', arr2)
arr3 = [7 for i in range(5)]
print(f'c)', arr3)
arr4 = [i for i in range(1,10)]
print(f'd)', arr4)
arr5 = [i*2 for i in range(1,10)]
print(f'e)', arr5)
arr6 = [random.randint(1,20) for i in range(10)]
print(f'f)', arr6)
arr7 = [[] for i in range(5)]
print(f'g)', arr7)
arr8 = [[1 for i in range(2)] for j in range(4)]
print(f'h)', arr8)
arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
print(f'i)', arr9)
arr10=[4,0,3]
arr11=[0 for i in range(15)]
print(f'k)', arr11)
arr12=[random.randint(0,1) for i in range(20)]
print(f'm', arr12)
arr13=[i for i in range(1,31)]
print(f'l)', arr13)
arr14=[[False for i in range(5)] for j in range(2)]
print(f'n)', arr14)