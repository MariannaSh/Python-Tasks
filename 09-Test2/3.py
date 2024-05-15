def f(array2D):
    for i in range(len(array2D)):
        sum_col=0
        sum_row=0
        for j in range(len(array2D)):
            sum_row+=array2D[i][j]
            sum_col+=array2D[j][i]
        if sum_col!=sum_row:
            return False
        return True
    


print(f([[3,7,2],[4,2,5],[5,2,1]]) )
print(f([[3,7,2],[4,2,5],[9,2,1]]))

