import sys
input = sys.stdin.readline
arr = []
for _ in range(int(input())):
    xy = list(map(int, input().split()))
    arr.append(xy)

arr.sort(key=lambda arr: (arr[0], arr[1]))

for i in range(len(arr)):
    print(*arr[i])