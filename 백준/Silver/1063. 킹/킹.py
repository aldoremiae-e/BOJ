order = {
    # i, j
    'R': (0, 1),
    'L': (0, -1),
    'B': (1, 0),
    'T': (-1, 0),
    'RT': (-1, 1),
    'LT': (-1, -1),
    'RB': (1, 1),
    'LB': (1, -1)
}

king, stone, N = map(str, input().split())
kj, ki = ord(king[0]) - 65, 8 - int(king[1])
sj, si = ord(stone[0]) - 65, 8 - int(stone[1])
N = int(N)
for i in range(N):
    od = input()
    di, dj = order[od]
    cki, ckj = di + ki, dj + kj
    if (0 <= cki < 8 and 0 <= ckj < 8):
        if cki == si and ckj == sj:
            csi, csj = di + si, dj + sj
            if (0 <= csi < 8 and 0 <= csj < 8):
                si, sj = csi, csj
                ki, kj = cki, ckj
            else:
                continue
        else:
            ki, kj = cki, ckj
kj, sj = chr(kj + 65), chr(sj + 65)
ki, si = 8 - ki, 8 - si

print(kj, ki, sep='')
print(sj, si, sep='')