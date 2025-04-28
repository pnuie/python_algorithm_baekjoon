def cal_chicken_distance(selected_chicken):
    global ans
    now_ans = ans
    chicken_distance = 0
    for i in range(len(house)):
        min_dist = 1e9
        house_xy = house[i]
        #각 집에서 치킨집까지의 최소 거리를 구함
        for j in range(len(selected_chicken)):
            chicken_xy = selected_chicken[j]
            distance = abs(house_xy[0] - chicken_xy[0]) + abs(house_xy[1] - chicken_xy[1])
            if min_dist >= distance: min_dist = distance
        #최소거리를 모든 집에 대해 구하여 더 해줌 -> 도시의 치킨 거리
        chicken_distance += min_dist
        #더하다가 현재 구한 치킨거리보다 크면 더이상 계산하지 않음. 가지치기.
        if now_ans < chicken_distance: return now_ans
    return chicken_distance

import sys
import copy
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            house.append([i, j])
        if matrix[i][j] == 2:
            chicken.append([i, j])

chicken_comb = []

comb = list(combinations(chicken, m))
for i in range(len(comb)):
    chicken_comb.append(list(comb[i]))

selected_chicken = []
ans = 1e9

for i in range(len(chicken_comb)):
    temp = cal_chicken_distance(chicken_comb[i])
    ans = min(ans, temp)

print(ans)