from sys import stdin

nums = list(map(int, stdin.readline().split()))
ans = 0
for i in nums:
    ans += i*i
print(ans%10)