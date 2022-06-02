# n은 20이하의 자연수 또는 0
n = int(input())
a = [0] * (n+1)

for i in range(n+1):
    if i == 0:      # n = 0일 때를 고려하여, i == 0 일 때를 고려해야함
        a[i] = 0
    elif i == 1:
        a[i] = 1
    else:
        a[i] = a[i-1] + a[i-2]
print(a[-1])