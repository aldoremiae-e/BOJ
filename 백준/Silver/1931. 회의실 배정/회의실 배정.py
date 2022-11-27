from sys import stdin
from collections import deque
N = int(stdin.readline())
lst = deque()

'''
그리디 알고리즘 (탐욕 알고리즘)

정렬 순
1. 끝나는 시간이 빠른 순서대로 정렬
2. 시작하는 시간이 빠른 순서대로
sort 속 정렬 옵션 ( key = lambda )
'''

for _ in range(N):
    s, e = map(int, stdin.readline().split())
    lst.append((s, e))
# 정렬조건 1, 2
lst = sorted(lst, key=lambda x : (x[1], x[0]))
# 시작시간가 이전 끝나는시간보다 크거나 같아야함.
cnt = 0
end_time = 0
for i in lst:
    s, e = i[0], i[1]
    if s >= end_time:
        cnt += 1
        end_time = e

print(cnt)