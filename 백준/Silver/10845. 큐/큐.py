import sys
N = int(input())
q = []
for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        q.append(order[1])
    elif order[0] == 'pop':
        print(q.pop(0) if q else -1)
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        print(1 if not q else 0)
    elif order[0] == 'front':
        print( -1 if not q else q[0])
    elif order[0] == 'back':
        print(-1 if not q else q[-1])