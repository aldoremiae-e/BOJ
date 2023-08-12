s = input().rstrip()
N = len(s)
a = 0
for i in range(N-1):
    if s[i] == s[i+1]:
        a += 5
    else:
        a += 10
print(a+10)