maps = [list(map(str, input().strip())) for _ in range(8)]
cnt = 0
for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0 and maps[i][j] == 'F':
            # i짝수 j짝수 # 말이있을때
            cnt += 1
        if i % 2 == 1 and j % 2 == 1 and maps[i][j] == 'F':
            cnt += 1
print(cnt)