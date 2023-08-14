n, k = map(int, input().split())
def fact(i):
    if i == 1:
        return memo[i]
    if i not in memo:
        memo[i] = fact(i-1) * i
    return memo[i]
def solve(n, k):
    return (fact(n) // (fact(n-k) * fact(k))) % 10007
memo = {}
memo[1] = 1
if k == 0 or k == n:
    print(1)
else:
    print(solve(n, k))
