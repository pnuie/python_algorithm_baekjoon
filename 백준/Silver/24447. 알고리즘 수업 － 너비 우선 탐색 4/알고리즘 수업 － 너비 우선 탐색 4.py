from collections import deque
import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())

visited = [0] * (N + 1)
depth = [-1] * (N + 1)

g = [[] for _ in range(N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    g[i].append(j)
    g[j].append(i)

count = 1
def bfs(v):
    global count
    dq = deque([R])
    depth[R]=0
    while dq:
        v = dq.popleft()
        for x in g[v]:
            if depth[x] == -1:
                count += 1
                depth[x] = depth[v] + 1
                visited[x] = count
                dq.append(x)

for i in range(1, N + 1):
    g[i].sort(reverse = False)

bfs(R)

ans = 0

for i in range(1, N+1):
    ans += depth[i]*visited[i]

print(ans)