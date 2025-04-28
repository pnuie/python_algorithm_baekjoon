h, m = list(map(int, input().split()))

if m < 45 :
    if h == 0 : print(23, 60-(45-m))
    else: print(h-1, 60-(45-m))
else: print(h, m-45)
