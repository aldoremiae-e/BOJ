import sys
T = int(input())
for tc in range(T):
    sentence = sys.stdin.readline().split()
    for s in sentence:
        print(s[::-1], end=' ')