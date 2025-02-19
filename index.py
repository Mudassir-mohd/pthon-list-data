# 1. Diagonal Elements Sum
def diagonal_sum(matrix, diagonal='primary'):
    n = len(matrix)
    total = 0
    
    if diagonal == 'primary':
        for i in range(n):
            total += matrix[i][i]
    elif diagonal == 'secondary':
        for i in range(n):
            total += matrix[i][n - 1 - i]
    else:
        raise ValueError("Invalid diagonal type. Choose 'primary' or 'secondary'.")
    
    return total


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Primary Diagonal Sum:", diagonal_sum(matrix, 'primary')) 
print("Secondary Diagonal Sum:", diagonal_sum(matrix, 'secondary')) 





# 2. Add Two Matrices
def add_matrices(matrix1, matrix2):
    # Check if both matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions")
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    
    # Add corresponding elements
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return result

# Example usage:
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = add_matrices(matrix1, matrix2)
for row in result:
    print(row)
