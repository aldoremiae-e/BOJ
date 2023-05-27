from collections import deque
s = input()
lst = []
rev = deque()
i = 0
while i < len(s):
    if s[i] == '<':
        while rev:
            lst.append(rev.pop())
        lst.append(s[i])
        for j in range(i+1, len(s)):
            if s[j] == '>':
                lst.append(s[j])
                i = j+1
                break
            lst.append(s[j])
    elif s[i] == ' ':
        while rev:
            lst.append(rev.pop())
        lst.append(s[i])
        i += 1
    else:
        rev.append(s[i])
        i += 1
while rev:
    lst.append(rev.pop())
print(*lst, sep='')