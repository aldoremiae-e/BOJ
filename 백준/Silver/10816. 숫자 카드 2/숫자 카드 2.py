from collections import Counter
import sys
N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
cards = Counter(cards)
M = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))
for l in check:
    print(cards[l], end=' ')