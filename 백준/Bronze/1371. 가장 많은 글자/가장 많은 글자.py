import sys

input = sys.stdin.read

a = input().replace("\n", "").replace(" ", "")
c = [0] * 26
for i in a:
    c[ord(i) - 97] += 1

max_num = max(c)
lst = []
for i in range(26):
    if c[i] == max_num:
        lst.append(chr(i + 97))

lst.sort()
print(*lst, sep="")