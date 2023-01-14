from sys import stdin

N = int(stdin.readline())
arr = [list(map(int, stdin.readline().strip())) for _ in range(N)]
lst = []
def conquer(i, j, n):
    global lst
    color = arr[i][j]
    flag = 1
    for x in range(i, i + n):
        if flag == 0:
            break
        for y in range(j, j + n):
            if arr[x][y] != color:
                lst.append('(')
                flag = 0
                # divide
                conquer(i, j, n//2)
                conquer(i, j + n//2, n//2)
                conquer(i + n//2, j, n//2)
                conquer(i + n//2, j + n//2, n//2)
                lst.append(')')
                break
    if flag == 1:
        if color == 0:
            lst.append('0')
        else:
            lst.append('1')

conquer(0, 0, N)
print(''.join(lst))