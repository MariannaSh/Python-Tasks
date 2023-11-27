def f(number):
    array=[3,2,5,6,4,34]
    count=0
    for i in array:
        if i>number:
            count+=1
    return count

print(f(1))
