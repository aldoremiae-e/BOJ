a = int(input())
b,c = map(int, input().split())
ret = min(a, (b // 2) + c)
print(ret)