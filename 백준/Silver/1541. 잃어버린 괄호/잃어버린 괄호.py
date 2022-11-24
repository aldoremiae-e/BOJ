from sys import stdin
from collections import deque
# 입력
exp = stdin.readline().rstrip()
a = ''
lst = deque([])
for i in range(len(exp)):
  if exp[i].isdigit():
    a += exp[i]
  else:
    lst.append(int(a))
    lst.append(exp[i])
    a = ''
  if i == (len(exp)-1):
    lst.append(int(a))

res = deque([])
num = 0
for j in range(len(lst)):
  if lst[j] == '-':
    res.append(num)
    num = 0   
  elif type(lst[j]) == int:
    num += lst[j]
  if j == len(lst)-1:
    res.append(num)

result = res[0]
for l in range(1, len(res)):
  result -= res[l]
print(result)