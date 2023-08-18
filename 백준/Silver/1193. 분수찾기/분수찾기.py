i, j, k = 1, 1, 1
flag = True
N = int(input())
# 내려가기 => j == 1일때
# 대각선 올라가기 => i가 일이 될 때 까지
# 오른쪽으로 => i == 1일때
# 대각선 내려가기 => j가 1이 될 때까지

if N == 1:
    print(f'{i}/{j}')
else:
    while True:
        j += 1
        k += 1
        if k == N:
            break
        while j > 1:
            i += 1
            j -= 1
            k += 1
            if k == N:
                break
        if k == N:
            break

        i += 1
        k += 1
        if k == N:
            break
        while i > 1:
            i -= 1
            j += 1
            k += 1
            if k == N:
                break
        if k == N:
            break
    print(f'{i}/{j}')