arr = list(map(int, input().split()))

num = 1
while True:
    cnt = 0
    for i in arr:
        if (num % i) == 0:
            cnt += 1
    if cnt >= 3:
        print(num)
        break
    else:
        num += 1