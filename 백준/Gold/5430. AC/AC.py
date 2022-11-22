# AC
# R 순서를 뒤집는 D popleft
# []인데 D 쓰면 error

from sys import stdin
from collections import deque

T = int(stdin.readline())
for tc in range(1, T+1):
  p = stdin.readline().rstrip()
  n = int(stdin.readline())
  revlst = deque()
  if n > 0:
    lst = deque(map(int, stdin.readline().lstrip('[').rstrip().rstrip(']').split(',')))
  else:
    emptylst = stdin.readline()
    lst = deque([])
  flag = 1 # 정방향
  errorflag = 0
  for func in p:
    # R
    if func == 'R':
      # reversed를 이용하면 시간초과남
      flag *= -1
    # D
    elif func == 'D':
      if lst:
        if flag > 0:
          lst.popleft()
        else:
          lst.pop()
      else:
        errorflag = 1
        print('error')
        break
  
  if errorflag == 0:
    if flag < 0:
      for i in range(len(lst)-1,-1,-1):
        revlst.append(lst[i])
      lst = revlst
    print('[', end='')
    print(*lst, sep=',', end='')
    print(']')