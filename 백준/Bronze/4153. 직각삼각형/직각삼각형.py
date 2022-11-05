from collections import deque
while 1:
    arr = deque(list(map(int, input().split())))
    if (arr[0]==0 and arr[1]==0 and arr[2]==0):
        break
    for i in range(3):
        if arr[i] == max(arr):
            c = arr[i]
        elif arr[i] == min(arr):
            a = arr[i]
        else:
            b = arr[i]

    if (a**2 + b**2) == c**2:
        print('right')
    else:
        print('wrong')