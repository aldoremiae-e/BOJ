N = int(input())
n = N
cnt = 0
while True:
    new = (n % 10) * 10 + (n // 10 + n % 10) % 10
    if new == N:
        cnt += 1
        break
    else:
        n = new
        cnt += 1
print(cnt)