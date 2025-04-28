arr = [ord(x)-65 for x in input()]
for i in range(len(arr)):
    if arr[i] < 3 :
        arr[i] = 3
    elif arr[i] < 6 :
        arr[i] = 4
    elif arr[i] < 9 :
        arr[i] = 5
    elif arr[i] < 12 :
        arr[i] = 6
    elif arr[i] < 15 :
        arr[i] = 7
    elif arr[i] < 19 :
        arr[i] = 8
    elif arr[i] < 22 :
        arr[i] = 9
    else : arr[i] = 10
print(sum(arr))