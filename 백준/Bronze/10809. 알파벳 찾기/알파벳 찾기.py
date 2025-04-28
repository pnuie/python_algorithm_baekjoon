arr = [x for x in input()]
visit = [-1 for _ in range(26)]

for i in range(len(arr)):
    if visit[ord(arr[i])-97] == -1:
        visit[ord(arr[i])-97] = i

print(*visit)