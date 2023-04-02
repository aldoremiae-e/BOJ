h, m, s = map(int, input().split())
d = int(input())
time = h*3600 + m*60 + s + d
time = time % (3600 * 24)
eh = int((time // 3600))
em = int((time % 3600) // 60)
es = int(time % 60)
print(eh, em, es)