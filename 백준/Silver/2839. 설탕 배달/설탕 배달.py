N = int(input())

arr =[]
for i in range(N//5+1):
    for j in range(N//3+1):
        if N == 5*i + 3*j:
            arr.append(i+j)

if arr : print(min(arr))
else : print(-1)