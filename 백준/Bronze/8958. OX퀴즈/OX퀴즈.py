from sys import stdin
T = int(stdin.readline())
for tc in range(T):
  arr = stdin.readline()
  cnt = 0
  ans = 0
  for i in arr:
    if i == 'O':
      cnt += 1
      ans += cnt
    else:
      cnt = 0
  print(ans)