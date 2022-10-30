import sys
from collections import deque
bracket = list(sys.stdin.readline())
stack = deque([])
cnt = 0
ans = 0
for i in range(len(bracket)):
    if bracket[i] == '(':
        cnt += 1
        stack.append(bracket[i])

    elif bracket[i] == ')':
        if bracket[i-1] == '(':
            # i-1과 i는 레이저
            stack.pop()
            cnt -= 1
            ans += cnt

        else:
            # 닫힌괄호
            stack.pop()
            ans += 1
            cnt -= 1

print(ans)