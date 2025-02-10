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
        x[i] /= matrix[i][i]
    
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
print("------------------------------------------------")

A = [
    [1, 2, -1, 3],
    [2, -1, 3, -2],
    [-3, 4, 1, 1],
    [5, -2, 2, 4]
]
B = [5, 3, -2, 7]

solution = solve_matrix(A, B) 
print("Solution:", solution)
print("------------------------------------------------")

A = [
    [2, 1, -3, 4],
    [1, -4, 2, -2],
    [3, 2, 1, 5],
    [-1, 3, 2, 1]
]
B = [6, -3, 7, 2]

solution = solve_matrix(A, B) 
print("Solution:", solution)
print("------------------------------------------------")

A = [
    [4, -2, 3, 1],
    [3, 5, -1, -4],
    [2, 1, 6, -3],
    [0, -1, 2, 4]
]
B = [8, 1, 5, -2]

solution = solve_matrix(A, B) 
print("Solution:", solution)
print("------------------------------------------------")
