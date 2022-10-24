n, m = list(map(int, input().split()))

if n < m:
  print('<')
elif n == m:
  print('==')
else:
  print('>')