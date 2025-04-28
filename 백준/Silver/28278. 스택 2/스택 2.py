class stack():
    def __init__(self):
        self.arr = []

    def push(self, X):
        self.arr.append(X)

    def pop(self):
        try:
            print(self.arr.pop())
        except:
            print(-1)

    def count(self):
        print(len(self.arr))

    def isempty(self):
        if self.arr: print(0)
        else: print(1)

    def top(self):
        try: print(self.arr[-1])
        except: print(-1)

import sys
N = int(input())
mystack = stack()
for _ in range(N):
    num = sys.stdin.readline().rstrip('\n)')
    if len(num) == 1:
        num = int(num)
    else: num, X = map(int, num.split())
    if num == 1: mystack.push(X)
    elif num == 2: mystack.pop()
    elif num == 3: mystack.count()
    elif num == 4: mystack.isempty()
    else : mystack.top()