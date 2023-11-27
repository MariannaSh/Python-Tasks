array=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range(1,6):
    for j in range(1,6):
        array[i - 1][j - 1] = i * j


for row in array:
    for value in row:
        print(f'{value:2d}' , end=' ') #value:2d - форматирование числа с использованием 2 позиций 02 (например)
    print()