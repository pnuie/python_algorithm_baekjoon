arr = list(int(x) for x in input())
arr.sort(reverse=True)
print(*arr,sep='')