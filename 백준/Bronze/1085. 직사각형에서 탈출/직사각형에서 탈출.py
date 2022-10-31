x, y, w, h = list(map(int, input().split()))
print(min(x-0, w-x, h-y, y-0))