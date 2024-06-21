def parse_matrix(matrix_str):
    rows = matrix_str.split('|')
    matrix = {}
    for i, row in enumerate(rows):
        matrix[i] = list(map(int, row.split(',')))
    return matrix

def matrix_mult(U, V):
    n = len(U)
    M = {i: [0] * n for i in range(n)}
    for i in range(n):
        for j in range(n):
            for k in range(n):
                M[i][j] += U[i][k] * V[k][j]
    return M

def matrix_to_string(matrix):
    result = []
    for i in sorted(matrix.keys()):
        result.append(str(matrix[i]))
    return '\n'.join(result)

def main():
    U_str = input("Enter matrix U: ")
    V_str = input("Enter matrix V: ")
    

    U = parse_matrix(U_str)
    V = parse_matrix(V_str)

    M = matrix_mult(U, V)

    print("M = U x V")
    print(matrix_to_string(M))

if __name__ == "__main__":
    main()
