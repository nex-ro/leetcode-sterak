def setZeroes(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    m = len(matrix[0])
    zero_col_index = []
    zero_row_index = []
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == 0:
                zero_row_index.append(row)
                zero_col_index.append(col)
    
    for row in range(n):
        for col in range(m):
            if row in zero_row_index or col in zero_col_index:
                matrix[row][col] = 0
    return matrix