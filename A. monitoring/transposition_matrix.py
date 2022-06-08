def transposition_matrix(rows, columns, matrix):
    trans_matrix = []
    for column in range(columns):
        trans_matrix.append([0]*rows)
    for i in range(len(matrix)):
        for j in range(columns):
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix


if __name__ == '__main__':
    n, m = int(input()), int(input())
    input_matrix = []
    for row in range(n):
        input_matrix.append(list(map(int, input().strip().split())))
    output_matrix = transposition_matrix(rows=n,
                                         columns=m,
                                         matrix=input_matrix)
    for i in range(len(output_matrix)):
        print(*output_matrix[i])
