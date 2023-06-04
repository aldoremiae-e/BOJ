Total = int(input())
N = int(input())
cal = 0

for i in range(N):
    a, b = map(int, input().split())
    cal += (a*b)
if cal == Total:
    print('Yes')
else:
    print('No')