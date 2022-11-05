# 카드개수 # 숫자
from collections import deque
from itertools import combinations
N, M = map(int, input().split())
cards = deque(list(map(int, input().split())))
# 카드 세장 합 < M 가장 가까운 값
ans = 0
#  조합
comb = list((combinations(cards, 3)))

for i in comb:
    x = sum(i)
    if x <= M:
        if ans <= x:
            ans = x
print(ans)