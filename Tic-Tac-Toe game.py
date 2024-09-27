def result_checking(row, column, right_to_left, left_to_right):
    abhinav = ["O", "O", "O"]
    anjali = ["X", "X", "X"]
    if anjali == right_to_left or anjali == left_to_right:
        print("Anjali Wins")
    elif abhinav == right_to_left or abhinav == left_to_right :
        print("Abhinav Wins")
    elif abhinav in row or abhinav in column:
        print("Abhinav Wins")
    elif anjali in row or anjali in column:
        print("Anjali Wins")
    else:
        print("Tie")


def creating_row_column_diagonals(matrix):
    left_to_right = []
    right_to_left = []
    row = []
    column = []
    for i in range(3):
        each_row = []
        each_column = []
        left_to_right.append(matrix[i][i])
        right_to_left.append(matrix[2 - i][i])
        for j in range(3):
            each_row.append(matrix[i][j])
            each_column.append(matrix[j][i])
        row.append(each_row)
        column.append(each_column)
        
    return row, column, right_to_left, left_to_right
        

matrix = []
for i in range(3):
    row = input().split()
    each_row = []
    for j in row:
        each_row.append(j)
    matrix.append(each_row)

row, column, right_to_left, left_to_right = creating_row_column_diagonals(matrix)

result_checking(row, column, right_to_left, left_to_right)
