n, m = map(int, input().split())
arr = [x for x in range(n+1)]

'''
1. 원래 수열을 부분 추출한다.
2. 부분 추출한 수열을 뒤집는다.
3. 뒤집은 수열을 다시 끼운다.
음....
'''
def partial_reverse(arr, a, b):
    partial_arr = arr[a:b+1]
    rev_arr = list(reversed(partial_arr))
    k = 0
    for i in range(a,b+1):
        arr[i] = rev_arr[k]
        k += 1

while 1:
    try:
        a, b = map(int, input().split())
        partial_reverse(arr,a,b)
    except : break

for i in range(1, len(arr)):
    print(arr[i], end=' ')