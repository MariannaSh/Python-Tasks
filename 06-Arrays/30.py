
def bubblesort(array):
    for j in range(len(array)-1): #количество раз которое мы должны повторять обходы по циклу
        for i in range(len(array)-1): #один обход
            if array[i]>array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
    return array

print(bubblesort([3,1,8,5]))
print(bubblesort([9,3,2,5,1]))
print(bubblesort([7,3,0,4,4]))