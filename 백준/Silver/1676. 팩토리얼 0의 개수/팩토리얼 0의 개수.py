from sys import stdin

N = int(stdin.readline())
ans = 1
for i in range(1, N+1):
  ans *= i
ans =str(ans)
cnt = 0

for j in range(len(ans)-1,-1,-1):
  if ans[j] == '0':
    cnt += 1
  else:
    if cnt == 0:
      continue
    else:
      break
print(cnt)