from sys import stdin

word = stdin.readline().rstrip()
word = word.lower()
alpha = {}
for i in word:
    if i in alpha:
        alpha[i] += 1
    else:
        alpha.update({i: 1})
mnum = max(alpha.values())
cnt = 0
malpha = ''
for key, val in alpha.items():
    if val == mnum:
       cnt += 1
       malpha = key
if cnt > 1:
    print('?')
else:
    print(malpha.upper())