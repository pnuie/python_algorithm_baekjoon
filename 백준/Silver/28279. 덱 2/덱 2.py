from collections import deque


class mydeque:
    def __init__(self):
        self.arr = deque()

    def appendleft(self, X):
        self.arr.appendleft(X)

    def append(self, X):
        self.arr.append(X)

    def popleft(self):
        try:
            print(self.arr.popleft())
        except:
            print(-1)

    def pop(self):
        try:
            print(self.arr.pop())
        except:
            print(-1)

    def count(self):
        print(len(self.arr))

    def isempty(self):
        if not self.arr:
            print(1)
        else: print(0)

    def head(self):
        try:
            print(self.arr[0])
        except:
            print(-1)

    def tail(self):
        try:
            print(self.arr[-1])
        except:
            print(-1)

import sys
input = sys.stdin.readline
mydeque = mydeque()
N = int(input())
for _ in range(N):
    code = input().rstrip('\n')

    if len(code) > 1:
        code, X = map(int, code.split())
    else:
        code = int(code)

    # try:
    #     print(code, X)
    # except:
    #     print(code)

    if code == 1:
        mydeque.appendleft(X)

    if code == 2:
        mydeque.append(X)

    if code == 3:
        mydeque.popleft()

    if code == 4:
        mydeque.pop()

    if code == 5:
        mydeque.count()

    if code == 6:
        mydeque.isempty()

    if code == 7:
        mydeque.head()

    if code == 8:
        mydeque.tail()

    # print(mydeque.arr)
    # print('-'*20)