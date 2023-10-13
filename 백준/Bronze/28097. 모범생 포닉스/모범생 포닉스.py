N = int(input())
lst = list(map(int, input().split()))
a = sum(lst) + (8 * (N-1))
d = a // 24
h = a % 24
print(d, h)