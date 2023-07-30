memo = {}
memo[(20, 20, 20)] = 1048576
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    def dp(a, b, c):
        if (a, b, c) not in memo:
            if a <= 0 or b <= 0 or c <= 0:
                memo[(a, b, c)] = 1
                return 1
            if a > 20 or b > 20 or c > 20:
                memo[(a, b, c)] = 1048576
                return 1048576
            if a < b and b < c:
                num = dp(a, b, c-1) + dp(a, b-1, c-1) - dp(a, b-1, c)
            else:
                num = dp(a-1, b, c) + dp(a-1, b-1, c) + dp(a-1, b, c-1) - dp(a-1, b-1, c-1)
            memo[(a, b, c)] = num
        return memo[(a, b, c)]
    ans = dp(a, b, c)
    print(f'w({a}, {b}, {c}) = {ans}')