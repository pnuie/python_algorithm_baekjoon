import sys
input = sys.stdin.readline
n = int(input())

flower = [list(map(int, input().split())) for _ in range(n)]

flower.sort(key=lambda f: (-f[2], -f[3]))

# for i in range(n):
#     print(flower[i])
# 
# print('-'*20)

def check_feasible(candidate, last_flower) :
    if candidate[0] < last_flower[2]: return True #후보꽃 시작 월이 마지막 꽃의 지는 월보다 작으면 True
    if candidate[0] == last_flower[2]: #서로 월이 같으면 일까지 확인해야함
        if candidate[1] <= last_flower[3]: return True
    else : return False

ans = 0
temp = 0
arr = []
last_flower = [0, 0, 3, 1]

while 1:
    if not ans == temp :
        print(0)
        exit()
    for x in flower:
        if check_feasible(x, last_flower) :
            arr.append(x)
            last_flower = x
            flower.remove(x)
            ans += 1
            break
    temp += 1
    if last_flower[2] >= 12 : break

# print(arr)
print(ans)