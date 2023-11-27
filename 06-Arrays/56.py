
def f2(m):
    new_arr=[]
    for row in m:
        new_arr.extend(row) #append не подходит, потому что он копирует тоже самое,
                            #а extend добавляет конкретно числа
    return new_arr

print(f2([[2,3],[1,5]]))
