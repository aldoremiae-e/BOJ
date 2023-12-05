N = int(input())

memo = {}
memo[0] = 3
def top_down(n, idx):
    # base-case
    if n == 1:
        print("m")
        exit()
    elif 1 < n <= 3:
        print("o")
        exit()

    memo[idx] = memo[idx-1] * 2 + (idx + 3)

    if memo[idx] < n:
        top_down(n, idx+1)

    if memo[idx-1] + 1 == n:
        print("m")
        exit()
    elif n <= memo[idx-1] + idx + 3:
        print("o")
        exit()
    else:
        top_down(n - (memo[idx-1] + idx + 3), 1)
top_down(N, 1)