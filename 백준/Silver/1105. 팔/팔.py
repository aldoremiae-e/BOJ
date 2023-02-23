from sys import stdin
L, R = map(str, stdin.readline().split())
if len(L) != len(R):
    print(0)
else:
    cnt = 0
    for i in range(len(L)):
        if L[i] == R[i]:
            if L[i] == '8':
                cnt += 1
            else:
                continue
        else:
            break
    print(cnt)