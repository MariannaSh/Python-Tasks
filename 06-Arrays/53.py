def identity_matrix(n):
    # Создаем пустую матрицу размера n x n
    matrix = [[0] * n for i in range(n)]
    
    # Заполняем диагональные элементы единицами
    for i in range(n):
        matrix[i][i] = 1
    
    return matrix

def display(matrix):
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()

rozmiary=[3,5,8]
for i in rozmiary:
    display(identity_matrix(i))
    print()


