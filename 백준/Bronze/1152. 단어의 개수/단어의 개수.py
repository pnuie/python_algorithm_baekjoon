arr = [x for x in input()]

cnt = 0
if arr[0] == ' ':
    cnt += 1
if arr[-1] == ' ':
    cnt += 1
    
print(arr.count(' ')+1-cnt)