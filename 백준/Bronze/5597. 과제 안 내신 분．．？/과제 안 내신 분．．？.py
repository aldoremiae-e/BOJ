from sys import stdin
arr = [0] * 31
for _ in range(28):
    a = int(stdin.readline())
    arr[a] = 1
for idx, val in enumerate(arr):
    if idx == 0:
        continue
    if val == 0:
        print(idx)