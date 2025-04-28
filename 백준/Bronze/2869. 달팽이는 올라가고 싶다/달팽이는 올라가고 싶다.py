import math

A, B, V = map(int, input().split())

temp = V-A

#temp = A*n - B*n

print(math.ceil(temp/(A-B))+1)