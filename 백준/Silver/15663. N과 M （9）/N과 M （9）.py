def bt(start) :
    global cnt
    if len(cand) == m :
        print(' '.join(map(str, cand)))
        return

    remember_me = 0 #이 변수로 중복된 수열을 출력하는 것을 방지...
    for i in range(0, n) :
        if not visited[i] and not remember_me == A[i]:
            cand.append(A[i])
            visited[i] = True
            remember_me = A[i]
            bt(start+1)
            cand.pop()
            visited[i] = False

import sys

input = sys.stdin.readline
n, m = list(map(int, input().split()))
A = list(map(int,input().split()))
A.sort()

visited = [False for _ in range(n)]

cand = []
save = []
cnt = 0
bt(0)
