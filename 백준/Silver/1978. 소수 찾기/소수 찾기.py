'''
소수 : 약수가 1과 자기자신
'''
N = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    if i == 1:
        cnt += 0
    else:
        measure = 0
        for j in range(1, i+1):
            if i % j == 0:
                measure += 1
        if measure == 2:
            cnt += 1
print(cnt)
