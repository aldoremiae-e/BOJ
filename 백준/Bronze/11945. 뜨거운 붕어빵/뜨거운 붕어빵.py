a, b = map(int, input().split())
for i in range(a):
    q = input()
    for j in range(len(q) - 1, -1, -1):
        print(q[j], end="")
    print()

