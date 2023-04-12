r1, c1, r2, c2 = map(int, input().split())
R, C = r2-r1+1, c2-c1+1
maps = [[0] * C for _ in range(R)]
maps_num = R * C
maxlen = 0
i, j = 0, 0 # 인덱스 -> 굳이 맵의 인덱스로 받지 않아도 된다. 가상의 맵을 생각하자
num = 1
cnt = 1
didx = 0
dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]

if r1 <= i <= r2 and c1 <= j <= c2:
    maps_num -= 1
    maps[i - r1][j - c1] = str(num)
    # 공백
    if maxlen < len(str(num)):
        maxlen = len(str(num))
num += 1
while maps_num > 0:
    for _ in range(cnt):
        i, j = i + dirs[didx][0], j + dirs[didx][1]
        if r1 <= i <= r2 and c1 <= j <= c2:
            maps_num -= 1
            maps[i-r1][j-c1] = str(num)
            # 공백
            if maxlen < len(str(num)):
                maxlen = len(str(num))
        num += 1

    didx = (didx + 1) % 4
    if didx == 0 or didx == 2:
        cnt += 1


for i in range(R):
    for j in range(C):
        # 공백 맞춰야한다
        print(f'{maps[i][j]:>{maxlen}}', end=' ')
    print()