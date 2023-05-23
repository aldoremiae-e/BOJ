def conquer(N, r, c, cnt):
    if N == 2:
        # 숫자출력
        if r == 0 and c == 0:
            print(cnt)
        elif r == 0 and c == 1:
            print(cnt+1)
        elif r == 1 and c == 0:
            print(cnt+2)
        elif r == 1 and c == 1:
            print(cnt+3)
        return
    # (0, 0) (0, 4) (4, 0) (4, 4)
    n = N//2
    num = n**2
    if r < n and c < n:
        # 2사분면
        conquer(n, r, c, cnt)
    elif r < n and c >= n:
        # 1사분면
        conquer(n, r, c-n, cnt + num)
    elif r >= n and c < n:
        # 3사분면
        conquer(n, r-n, c, cnt + num*2)
    elif r >= n and c >= n:
        # 4사분면
        conquer(n, r-n, c-n, cnt + num*3)

N, r, c = map(int, input().split())
# 맵을 줄이는 것이 아니고, 좌표(r, c)의 값을 줄이자
# 첫번째값만 가져와
conquer(2**N, r, c, 0)
