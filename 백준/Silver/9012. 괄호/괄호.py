import sys
T = int(input())
for tc in range(T):
    flag = 0
    lst = sys.stdin.readline()
    stack = []
    for l in lst:
        # 열림
        #print(stack)
        if l == '(':
            stack.append(l)
        elif l == ')':
            if stack:
                stack.pop()
            else:
                flag = -1
    if stack or flag == -1:
        print('NO')
    else:
        print('YES')