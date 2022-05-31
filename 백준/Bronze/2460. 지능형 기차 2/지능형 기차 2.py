people = 0
maxnum = 0
for _ in range(10):
    O, I = map(int, input().split())
    people -= O
    people += I

    maxnum = people if people > maxnum else maxnum
print(maxnum)