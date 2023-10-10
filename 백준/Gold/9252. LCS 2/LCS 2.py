a = list(map(str, input().rstrip()))
b = list(map(str, input().rstrip()))
board = [[''] * (len(a) + 1) for _ in range(len(b) + 1)]

for i in range(1, len(b)+1):
    for j in range(1, len(a)+1):
        if b[i-1] == a[j-1]:
            board[i][j] = board[i-1][j-1] + a[j-1]
        else:
            if len(board[i-1][j]) > len(board[i][j-1]):
                board[i][j] = board[i-1][j]
            else:
                board[i][j] = board[i][j-1]
LCS = len(board[-1][-1])
print(LCS)
if LCS > 0:
    print(board[-1][-1])