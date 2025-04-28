n = int(input())
arr = list(map(int, input().split()))
M = 0
for i in range(len(arr)):
    if M<arr[i]:
        idx = i
        M = arr[i]

arr = [x/M*100 for x in arr]

print((sum(arr))/(len(arr)))