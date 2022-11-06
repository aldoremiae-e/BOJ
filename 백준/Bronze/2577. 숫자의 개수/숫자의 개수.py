import sys
num = 1
for _ in range(3):
    num *= int(sys.stdin.readline())
num = str(num)
cntlst = [0 for i in range(10)]

for n in num:
    for i in range(10):
        if int(n) == i:
            cntlst[i] += 1
for ans in cntlst:
    print(ans)