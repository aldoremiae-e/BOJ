import sys
input = sys.stdin.readline
stack = []

N = int(input())
for _ in range(N):
    order = input().rstrip()

    if len(order) == 1:
        if order == '2':
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif order == '3':
            print(len(stack))
        elif order == '4':
            if stack:
                print(0)
            else:
                print(1)
        elif order == '5':
            if stack:
                print(stack[-1])
            else:
                print(-1)
    else:
        o, num = order.split()
        stack.append(int(num))