'''
N = 2^n
r , c = r행 c열
'''

N, r, c = map(int, input().split())
ans = 0
 # N번 재귀
while N != 0:
    # 분할 정복
    # 4분할 기준 L : (2**N)//2 == 2**(N-1)보다 큰지 작은지
    # while 할 때 N -= 1 을 해야하므로, 먼저 뺀다음 돌리는게 효율적이다.
    N -= 1
    L = 2 ** N # 4

    # 1사분면
    if r < L and c < L:
        ans += (L ** 2) * 0

    # 2사분면 - 열r은 그대로, 행c은 L만큼 왼쪽으로 땡겨줘
    elif r < L and c >= L:
        ans += (L ** 2) * 1
        c -= L
    # 3사분면 - 열r을 아래쪽으로 땡겨줘, 행c는 그대로
    elif r >= L and c < L:
        ans += (L ** 2) * 2
        r -= L
    #4사분면 - 열, 행 둘다 땡겨줘
    else:
        ans += (L ** 2) * 3
        r -= L
        c -= L

print(ans)