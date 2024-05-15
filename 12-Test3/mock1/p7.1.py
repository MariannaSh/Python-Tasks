def f(arr2D):
    # Перебираем столбцы
    for col1 in range(len(arr2D[0])):
        for col2 in range(col1 + 1, len(arr2D[0])):
            # Сравниваем суммы значений в двух столбцах
            sum_col1 = sum(row[col1] for row in arr2D)
            sum_col2 = sum(row[col2] for row in arr2D)
            if sum_col1 == sum_col2:
                return True

    # Если не найдено двух столбцов с одинаковой суммой
    return False

arr1 = [[3, 4, 2], [2, 2, 2, 0], [5, 0, 0, 5], [4, 7, 0, 2], [0, 2, 0, 0]]
print(f([[3,4,2],[5,1,6]]))  
print(f([[3,4,2],[5,1,7]]))
print(f([[3,4],[5,1],[4,7]]))
print(f([[3,4],[5,9],[4,7]]))