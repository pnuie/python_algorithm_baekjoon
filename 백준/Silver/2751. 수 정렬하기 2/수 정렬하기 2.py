import sys
input = sys.stdin.readline
arr = []
for i in range(int(input())):
    arr.append(int(input()))
arr.sort()
for i in range(len(arr)):
    print(arr[i])