import sys
N = int(input())
stack = []
for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        stack.append(order[1])
    elif order[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop(-1))
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)