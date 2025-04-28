import sys

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n

def bt(start, now, total_cost, depth) :
    global ans

    if depth == n :
        if cost[now][start] :
            total_cost += cost[now][start]
            if ans > total_cost :
                ans = total_cost
        return

    if total_cost > ans : return

    for i in range(n):
        if not visited[i] and cost[now][i] :
            visited[i] = 1
            bt(start, i, total_cost + cost[now][i], depth + 1)
            visited[i] = 0

ans = sys.maxsize

for i in range(n):
    visited[i] = 1
    bt(i, i, 0, 1)
    visited[i] = 0

print(ans)