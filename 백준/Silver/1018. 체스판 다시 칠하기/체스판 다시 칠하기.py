# 미해결
import sys
n, m = list(map(int, input().split()))
empty = [[0 for _ in range(8)] for _ in range(8)]
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

chess1 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
chess2 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
ans = 65
for y in range(n-8+1):
    for x in range(m-8+1):
        cnt1, cnt2 = 0, 0
        for i in range(8):
            for j in range(8):
                empty[i][j] = arr[i+y][j+x]
                # 체스1과 비교
                if empty[i][j] != chess1[i][j]:
                    cnt1 += 1
                # 체스2과 비교
                if empty[i][j] != chess2[i][j]:
                    cnt2 += 1
        if ans > min(cnt1, cnt2):
            ans = min(cnt1, cnt2)
print(ans)