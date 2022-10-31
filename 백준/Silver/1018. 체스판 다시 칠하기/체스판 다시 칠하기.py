import sys
n, m = list(map(int, input().split()))
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

chess1 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

ans = 65
for y in range(n-8+1):
    for x in range(m-8+1):
        cnt1 = 0
        for i in range(8):
            for j in range(8):
                # 체스1과 비교
                if arr[i+y][j+x] != chess1[i][j]:
                    cnt1 += 1
        ans = min(cnt1, 64-cnt1) if ans > min(cnt1, 64-cnt1) else ans
print(ans)