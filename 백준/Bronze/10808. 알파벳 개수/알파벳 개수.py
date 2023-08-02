ans = [0] * 26
s = input()
for i in range(len(s)):
    ans[int(ord(s[i]) -ord('a'))] += 1
print(*ans)
