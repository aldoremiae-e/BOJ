from sys import stdin
from collections import deque
N, M = map(int, stdin.readline().split())
nums = sorted(list(map(int, stdin.readline().split())))
lst, ans = [], set()
visited = [0] * N

def dfs(cnt):
    global ans
    if cnt == M:
        # 중복된 수열의 유무를 확인해야한다. for문을 안쓰고 쓰는 방법이 있을까
        # 중복을 제거하는 자료구조에 추가하자!
        # tuple은 hashable
        ans.add(tuple(lst))
        return

    for i in range(N):
        if visited[i] == 0:
            lst.append(nums[i])
            visited[i] = 1
        else:
            continue
        cnt += 1
        dfs(cnt)
        cnt -= 1
        visited[i] = 0
        lst.pop()
dfs(0)
for val in ans:
    print(*val)