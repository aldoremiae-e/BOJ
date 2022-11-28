from sys import stdin
from collections import deque

N = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]


'''
(1)Divide 모든 숫자가 같은게 아니라면, 4개로 문제를 나눈다
(2)Conquer 나눈 문제가 또 모든 숫자가 같은게 아니라면, Divide
그렇지 않으면 cnt += 1
(3)Combine Conquer한 문제를 통합하여 원래의 문제를 수행 => cnt 다더해?
'''

def check(x, y, n):
    global white, blue
    flag = 1
    color = arr[x][y]
    for j in range(y, y + n):
        if flag < 0:
            break
        for i in range(x, x + n):
            if arr[i][j] != color:
                flag = -1
                check(x, y, n//2)
                check(x, y+n//2, n//2)
                check(x+n//2, y, n//2)
                check(x+n//2, y+n//2, n//2)
                break

    if flag > 0:
        if color == 0:
            white += 1
        else:
            blue += 1

white, blue = 0, 0
check(0, 0, N)
print(white)
print(blue)