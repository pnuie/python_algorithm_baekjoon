import math
x, y = map(int, input().split())
print(abs(x*y)//math.gcd(x, y))