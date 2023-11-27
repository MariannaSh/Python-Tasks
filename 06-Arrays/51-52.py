array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print('Array ДО:')
for i in array:
    for j in i:
        print(f"{j:2d}", end=' ')
    print()

array[0],array[-1]=array[-1],array[0]
print()
print('Array ПОСЛЕ ИЗМЕНЕНИЙ:')

for i in array:
    for j in i:
        print(f'{j:2d}', end=' ')
    print()