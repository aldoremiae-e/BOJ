from sys import stdin

asc = (1, 2, 3, 4, 5, 6, 7, 8)
des = (8, 7, 6, 5, 4, 3, 2, 1)
arr = tuple(map(int, stdin.readline().split()))
if arr == asc:
    print('ascending')
elif arr == des:
    print('descending')
else:
    print('mixed')