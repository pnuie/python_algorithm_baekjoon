h, m = list(map(int, input().split()))
t = int(input())

a = (m+t)//60
b = (m+t)%60

if a >= 1 :
    h = h+a
    if h >= 24 :
        print(h-24, b)
    else : print(h, b)

else : print(h, b)