n, m = map(int, input().split())

matrix = []
while True :
    try:
        arr = list(map(int, input().split()))
        matrix.append(arr)
    except : break

matrix1 = matrix[:n]
matrix2 = matrix[n:]

result = [[matrix1[i][j] + matrix2[i][j]
               for j in range(len(matrix1[0]))]
               for i in range(len(matrix1))]

for i in range(len(result)):
    print(*result[i])