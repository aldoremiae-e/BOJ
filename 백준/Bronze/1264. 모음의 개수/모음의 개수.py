from sys import stdin
vowel = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
while 1:
    cnt = 0
    sentence = stdin.readline().rstrip()
    if sentence == '#':
        break
    for s in sentence:
        if s in vowel:
            cnt += 1
    print(cnt)