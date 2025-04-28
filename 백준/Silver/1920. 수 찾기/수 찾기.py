n = int(input())
arr1 = set(list(map(int, input().split())))
m = int(input())
arr2 = list(map(int, input().split()))
for x in arr2:
    if x in arr1:
        print(1)
    else: print(0)