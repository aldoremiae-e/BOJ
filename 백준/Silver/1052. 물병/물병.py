from sys import stdin

n, k = map(int, stdin.readline().split())
# 2진수로 바꿔서 1의 개수가 물통의 개수?
# 2진수로 바꾸기

ans = 0
while 1:
    if bin(n).count('1') <= k:
        print(ans)
        break
    # 상점에서 물을 추가해야함
    n += 1
    ans += 1