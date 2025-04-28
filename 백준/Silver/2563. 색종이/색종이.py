matrix = [[0 for i in range(100)] for j in range(100)]
n = int(input())

for _ in range(n):
    i, j = map(int, input().split())
    for row in range(i-1, i-1+10):
        for column in range(j-1,j-1+10):
            matrix[row][column] = 1
    
ans = 0
for i in range(100):
    ans += matrix[i].count(1)

print(ans)