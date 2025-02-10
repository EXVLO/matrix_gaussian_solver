def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{num:7.3f}" for num in row))
    print()

def solve_matrix(matrix, results):
    n = len(matrix)
    
    for i in range(n):
        matrix[i].append(results[i])
    
    print("Initial augmented matrix:")
    print_matrix(matrix)
    
    for i in range(n):
        pivot = matrix[i][i]
        if pivot == 0:
            print("Error: Zero pivot encountered")
            return 0
        
        for j in range(i, n + 1):
            matrix[i][j] /= pivot
        
        for k in range(i + 1, n):
            factor = matrix[k][i]
            for j in range(i, n + 1):
                matrix[k][j] -= factor * matrix[i][j]
        
        print(f"Matrix after eliminating column {i}:")
        print_matrix(matrix)
    
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = matrix[i][n]
        for j in range(i + 1, n):
            x[i] -= matrix[i][j] * x[j]
    
    return x

A = [
    [2, 1, -1, 3],
    [-3, -1, 2, -1],
    [-2, 1, 2, 2],
    [1, 1, -1, 3]
]
B = [8, -11, -3, 4]

solution = solve_matrix(A, B) 
print("Solution:", solution)
