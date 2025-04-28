import sys
input = sys.stdin.readline
arr = set()
while 1:
    try:
        n  = int(input())
        arr.add(n%42)
    except: break
print(len(arr))
