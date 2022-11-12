import sys
from collections import deque
# 포켓몬 수 문제 수 1 < n,m < 100000
N, M = map(int, sys.stdin.readline().split())
# len(lst) = N, 포켓몬 번호 = lst idx + 1
# 포켓몬 이름 Poketmon, PoketmoN 2 <= len(name) <= 20
# 리스트 => 시간초과, 딕셔너리로 하자
dogam = dict()
for i in range(N):
    dogam[i] = sys.stdin.readline().rstrip()
# M 개의 줄 - 알파벳이면 번호, 번호이면 알파벳
dogam2 = {v:k for k,v in dogam.items()}
for _ in range(M):
    qes = sys.stdin.readline().rstrip()
    if qes.isdigit():
        # 번호
        print(dogam[int(qes)-1])
    else:
        # 이름
        print(dogam2[qes]+1)