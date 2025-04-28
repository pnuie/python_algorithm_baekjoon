import sys

input = sys.stdin.readline
n = int(input())

while 1:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except: break