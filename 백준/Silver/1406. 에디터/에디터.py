# L왼쪽 D오른쪽 B삭제 P문자열 추가

cre = list(map(str, input()))
N = len(cre)
M = int(input())
s = []
for _ in range(M):
    order = list(map(str, input().split()))
    if order[0] == 'P':
        cre.append(order[1])
    elif order[0] == 'L':
        if cre:
            s.append(cre.pop())
    elif order[0] == 'D':
        if s:
            cre.append(s.pop())
    elif order[0] == 'B':
        if cre:
            cre.pop()
    #print(cre)
while s:
    cre.append(s.pop())
print("".join(cre))