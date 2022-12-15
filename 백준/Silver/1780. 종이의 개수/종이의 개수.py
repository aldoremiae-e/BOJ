from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())
paper = list(list(map(int, stdin.readline().split())) for _ in range(N))
minus, zero, plus = 0, 0, 0
def conquer(i, j, n):
    global minus, zero, plus
    flag = 1
    num = paper[i][j]
    for x in range(i, i + n):
        if flag == 0:
            break
        for y in range(j, j + n):
            if paper[x][y] != num:
                flag = 0
                # divide
                conquer(i, j, n//3)
                conquer(i, j + n//3, n//3)
                conquer(i, j + 2 * (n//3), n//3)
                conquer(i + n//3, j, n//3)
                conquer(i + n//3, j + n//3, n//3)
                conquer(i + n//3, j + 2 * (n//3), n//3)
                conquer(i + 2 * (n//3), j, n//3)
                conquer(i + 2 * (n//3), j + n//3, n//3)
                conquer(i + 2 * (n//3), j + 2 * (n//3), n//3)
                break
    #combine
    if flag == 1:
        if num == -1:
            minus += 1
        elif num == 0:
            zero += 1
        else:
            plus += 1
conquer(0, 0, N)
print(minus)
print(zero)
print(plus)