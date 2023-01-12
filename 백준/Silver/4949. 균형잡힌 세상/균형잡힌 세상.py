from sys import stdin
from collections import deque
string = ''
while 1:
    string += stdin.readline().rstrip()
    if string == '.':
        break
    if '.' not in string:
        continue
    q = deque()
    flag = 1
    for i in string:
        if i == '(' or i == '[':
            q.append(i)
        elif i == ']':
            if q:
                if q[-1] == '[':
                    q.pop()
                else:
                    flag = -1
                    break
            else:
                flag = -1
                break
        elif i == ')':
            if q:
                if q[-1] == '(':
                    q.pop()
                else:
                    flag = -1
                    break
            else:
                flag = -1
                break
    if q:
        print('no')
    elif flag == -1:
        print('no')
    else:
        print('yes')
    string = ''