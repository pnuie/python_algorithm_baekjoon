X = int(input())-1
idx = 1
temp = 0
if X == 0 :
    print(1)
    exit()
while True:
    temp += 6*idx
    if X <= temp: break
    idx += 1
print(idx+1)