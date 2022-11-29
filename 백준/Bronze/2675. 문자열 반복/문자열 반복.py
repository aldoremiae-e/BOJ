T = int(input())
for tc in range(T):
    R, S = map(str, input().split())
    R = int(R)
    for s in S:
        print(s*R, end='')
    print()