from collections import deque
import sys

sys.setrecursionlimit(10**9)

#불이 네 방향으로...
#지훈이랑 불이 동시에 움직여야 함... queue를 두 개?
#지훈이가 움직일 때마다 .을 숫자로 바꿔주면 됨.

r, c = map(int, input().split())
matrix = [list(map(str, list(sys.stdin.readline().rstrip()))) for _ in range(r)]

#R 행의 개수 , C 열의 개수
#지훈이가 이동하는 시간을 찍을거임. 미로 문제처럼.
#지훈이랑 불 둘다 토마토처럼
#이동하다가 가장자리에 숫자가 안 찍히면 탈출을 못한거임
time = [[0]*(c) for _ in range(r)]

def bfs():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue1 = deque([])
    queue2 = deque([])
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 'J':
                time[i][j] = 1
                queue1.append([i, j]) # appendleft, pop 이랑 똑같음
            if matrix[i][j] == 'F':
                queue2.append([i, j])

#    print(queue1) #지훈이 위치를 잘 찾았는지...
#    print(queue2) #불의 위치를 잘 찾았는지...
#불 여러개가 움직일 때마다 지훈이가 "한번" 움직여야됨
#불이 먼저 움직여야함
#지훈이가 가장자리에 도달했을 때 종료하면 시간이 좀 줄지 않을까....R, C가 1000까지 되기 때문에
#지금 코드는 'F'가 가득 찰 때까지 돌림. 불필요함.
#반복문 사이에 print(matrix)를 해보면 지훈이와 불의 이동 경로를 볼 수 있음
    while queue1 or queue2 :
        # for i in range(len(matrix)):
        #     print(matrix[i])
        # print('-------------')
        save2 = queue2
        queue2 = deque([])
        while save2:
            x, y = save2.popleft()
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if 0 <= nx < r and 0 <= ny < c :
                    if matrix[nx][ny] == '.' or matrix[nx][ny] == 'J' :
                        matrix[nx][ny] = 'F'
                        queue2.append([nx, ny])

        save1 = queue1
        queue1 = deque([])

        while save1:
            a, b = save1.popleft()
            for i in range(4):
                na = dx[i] + a
                nb = dy[i] + b
                if na >= r or nb >= c: return
                if 0 <= na < r and 0 <= nb < c and matrix[na][nb] == '.':
                    matrix[na][nb] = 'J'
                    time[na][nb] = time[a][b] + 1
                    queue1.append([na, nb])

bfs()

#가장자리에 있는 숫자만 list에 넣어줌
#가장자리에 숫자가 있다는 건 탈출에 성공했다는 뜻

list = []

for i in range(r):
    for j in range(c):
        if time[0][j] > 0: list.append(time[0][j])
        if time[r-1][j] > 0 : list.append(time[r-1][j])
    if time[i][0] > 0: list.append(time[i][0])
    if time[i][c-1] > 0: list.append(time[i][c-1])

# for i in range(len(time)):
#     print(time[i])
#
# for i in range(len(matrix)):
#     print(matrix[i])

if list :
    ans = min(list)
    print(ans)

else : print('IMPOSSIBLE')