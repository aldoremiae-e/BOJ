N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
visit = []
for i in range(N):
    visit.append(i+1)
#print(lst, visit)
stack = []
pm = []
i = 1
flag = 0
for l in lst:
    while l not in stack:
        stack.append(i)
        pm += '+'
        i += 1
    if l == stack[-1]:
        stack.pop()
        pm += '-'
    else:
        flag = -1
        break
if flag == -1:
    print('NO')
else:
    for a in pm:
        print(a)