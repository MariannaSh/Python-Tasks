array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

for row in array:
    for column in row:
        print(column, end=' ')
    print()

print("-"*8)

def transpose_matrix(m):
    return  list(map(list, zip(*m)))



for i in transpose_matrix([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10],[11, 12, 13, 14, 15]]):
    for j in i:
        print(j, end=' ')
    print()

print("-"*8)

for i in transpose_matrix([[1,2,3],[4,5,6],[7,8,9]]):
    for j in i:
        print(j, end=' ')
    print()

print("-"*8)

for i in transpose_matrix([[1,2,3,4,5],[6,7,8,9,0]]):
    for j in i:
        print(j, end=' ')
    print()
print("-"*8)

for i in transpose_matrix([[2,1],[3,5],[7,4]]):
    for j in i:
        print(j, end=' ')
    print()
print("-"*8)