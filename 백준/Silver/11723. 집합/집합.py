from sys import stdin
from collections import deque
M = int(stdin.readline().rstrip())
S = set()

def Add(a):
  global S
  S.add(a)

def Remove(a):
  global S
  if a in S:
    S.remove(a)

def Toggle(a):
  global S
  if a in S:
    S.remove(a)
  else:
    S.add(a)
    
for i in range(M):
  s= deque(map(str, stdin.readline().split()))
  if s[0] == 'add':
    Add(s[1])
  elif s[0] == 'remove':
    if s[1] in S:
      Remove(s[1])
  elif s[0] == 'check':
    if s[1] in S:
      print(1)
    else:
      print(0)
  elif s[0] == 'toggle':
    Toggle(s[1])
  elif s[0] == 'all':
    S = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12' ,
         '13', '14', '15', '16', '17', '18', '19', '20'}    
  elif s[0] == 'empty':
    S = set()