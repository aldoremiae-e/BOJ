from sys import stdin
from collections import deque
s = stdin.readline().rstrip()
S = []
for i in range(len(s)):
    S.append(s[i])
al = deque()
op = deque()
ans = []

for i in S:
    if i.isalpha():
        if op:
            if op[-1] == '(':
                ans.append(i)
            else:
                al.append(i)
        else:
            ans.append(i)
    elif i == '+' or i == '-':
        if op:
            if op[-1] == '(':
                op.append(i)
            elif op[-1] == '*' or op[-1] == '/':
                while al:
                    ans.append(al.pop())
                while op[-1] != '(':
                    ans.append(op.pop())
                    if not op:
                        break
                op.append(i)
            else:
                while al:
                    ans.append(al.pop())
                ans.append(op.pop())
                op.append(i)
        else:
            op.append(i)
    elif i == '*' or i == '/':
        if op:
            if op[-1] == '(':
                op.append(i)
            elif op[-1] == '*' or op[-1] == '/':
                while al:
                    ans.append(al.pop())
                while op[-1] == '*' or op[-1] == '/':
                    ans.append(op.pop())
                    if not op:
                        break
                op.append(i)
            else:
                while al:
                    ans.append(al.pop())
                op.append(i)
        else:
            op.append(i)
    elif i == '(':
        op.append(i)
    elif i == ')':
        while al:
            ans.append(al.pop())
        while op[-1] != '(':
            ans.append(op.pop())
            if not op:
                break
        op.pop()
while al:
    ans.append(al.pop())
while op:
    ans.append(op.pop())

print(''.join(ans))