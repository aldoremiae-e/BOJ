import sys
T = int(input())
for tc in range(T):
    ans = 0
    lst = sys.stdin.readline()
    stack = []
    for l in lst:
        # 열림
        #print(stack)
        if l == '(':
            stack.append(l)
        elif l == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
            else:
                ans = -1
    if stack or ans == -1:
        print('NO')
    else:
        print('YES')