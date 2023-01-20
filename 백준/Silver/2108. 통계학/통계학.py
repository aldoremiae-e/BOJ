from sys import stdin
from collections import Counter
N = int(stdin.readline())
num = []
# 입력
for _ in range(N):
    n = (int(stdin.readline()))
    num.append(n)
l = len(num)
# 산술평균
print(round(sum(num) / l))
# 중앙값
num = sorted(num)
print(num[l // 2])
# 최빈값
cnt = Counter(num)
order = cnt.most_common()
maxnum = order[0][1]
modes = []
for i in order:
    if i[1] == maxnum:
        modes.append(i[0])
if len(modes) == 1:
    print(modes[0])
else:
    print(modes[1])
# 범위
print(max(num)-min(num))