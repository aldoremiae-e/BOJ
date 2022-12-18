from sys import stdin
i = 1
while 1:
    L, P, V = map(int, stdin.readline().split())
    if L == 0 and P == 0 and V == 0:
        break
    a = V // P * L
    b = L if L < V % P else V % P
    print(f'Case {i}: {a + b}')
    i += 1