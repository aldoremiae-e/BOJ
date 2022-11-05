from collections import deque
import sys
N = int(input())
dic = deque([])

for _ in range(N):
    dic.append(sys.stdin.readline().rstrip())
# 중복을 없애줌
setlst = set(dic)
sortlst = []
for i in setlst:
    sortlst.append((len(i), i))
# 숫자순, 알파벳순으로 정렬
sortlst= sorted(sortlst)

for j in sortlst:
    print(j[1], end='\n')