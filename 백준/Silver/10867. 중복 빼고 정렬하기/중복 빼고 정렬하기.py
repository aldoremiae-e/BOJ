N = int(input())
lst = list(map(int, input().split()))
lst.sort()
s = set()
for i in lst:
    s.add(i)
print(*s)