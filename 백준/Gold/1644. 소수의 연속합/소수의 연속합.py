N = int(input())
# 소수 구하기 - 에라토스테네스 체
check = [False, False] + [True] * (N-1)
primes = []
for i in range(2, N+1):
    if check[i]:
        primes.append(i)
        for j in range(i+i, N+1, i):
            check[j] = False

# 연속된 소수의 합
l = len(primes)
ans = 0
flag = False
for i in range(l):
    a = primes[i]
    left, right = i, i+1
    if a == N:
        ans += 1
        break
    while right < l:
        if a == N:
            ans += 1
            break
        elif a < N:
            a += primes[right]
            right += 1
        else:
            break
print(ans)