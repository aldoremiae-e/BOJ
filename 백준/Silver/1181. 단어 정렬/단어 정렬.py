import sys
N = int(input())
setlst = set()

for _ in range(N):
    s = sys.stdin.readline().rstrip()
    setlst.add((len(s), s))
setlst = sorted(setlst)
for l in setlst:
    print(l[1])