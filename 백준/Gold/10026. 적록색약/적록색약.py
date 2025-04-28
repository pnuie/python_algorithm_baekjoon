import sys
import copy

input = sys.stdin.readline
n = int(input())
matrix = [list(map(str, list(sys.stdin.readline().rstrip()))) for _ in range(n)]

#matrix2 = matrix #이건 같은 객체를 가르키고 있는거라서 당연히 안됨.
#matrix2 = matrix.copy() #이것도 안됨. matrix2[0] = matrix[0] 이런 식으로 할당되어있음
matrix2 = copy.deepcopy(matrix)

# print(n)
# for i in range(n):
#     print(matrix[i])

#함수 2개를 만들어도 될 것 같음
#적록색약이 아닌 사람이 봤을 때 구역의 개수
#적록색약인 사람이 봤을 때 구역의 개수

def dfs1(x, y, X):
    matrix[x][y] = 0 #방문했으니까 0으로 바꿔줌
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = []
    q.append([x, y])
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == X:
                    q.append([nx, ny])
                    matrix[nx][ny] = 0

def dfs2(x, y, X):
    for i in range(n):
        for j in range(n):
            if matrix2[i][j] == 'G' : matrix2[i][j] = 'R'
    matrix2[x][y] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = []
    q.append([x, y])
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n and matrix2[nx][ny] == X:
                    q.append([nx, ny])
                    matrix2[nx][ny] = 0

cnt1 = 0
cnt2 = 0

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R' or matrix[i][j] == 'G' or matrix[i][j] == 'B':
            X = matrix[i][j]
            cnt1 += 1
            dfs1(i, j, X)

for i in range(n):
    for j in range(n):
        if matrix2[i][j] == 'R' or matrix2[i][j] == 'B':
            X = matrix2[i][j]
            cnt2 += 1
            dfs2(i, j, X)

print(cnt1, cnt2)