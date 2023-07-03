N = int(input())
lst = list(map(int, input().split()))
yans, mans = 0, 0
for i in range(N):
    y, m = lst[i], lst[i]
    # 영식
    while True:
        if y < 30:
            yans += 10
            break
        else:
            yans += 10
            y -= 30
    # 민식
    while True:
        if m < 60:
            mans += 15
            break
        else:
            mans += 15
            m -= 60
if yans > mans:
    print('M', mans)
elif yans < mans:
    print('Y', yans)
else:
    print('Y', 'M', mans)