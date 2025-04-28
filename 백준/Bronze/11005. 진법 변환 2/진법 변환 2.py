X, B = map(int, input().split())
s = ' '
arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while X:
    s += str(arr[X%B])
    X //= B

print(s[::-1])