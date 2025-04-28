n, m = map(int, input().split())
data1 = set(list(map(int, input().split())))
data2 = set(list(map(int, input().split())))

data3 = data1 - data2
data4 = data2 - data1

ans = data3 | data4
print(len(ans))