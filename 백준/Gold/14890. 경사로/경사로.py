# 길 2N개
# 경사로의 길이 L
N, L = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

def sol(lst):
    global visit, flag
    for j in range(1, N):
        if flag == 1:
            break
        if lst[j-1] == lst[j] - 1:
            if j >= L:
                for k in range(j-L, j):
                    # 경사로 X
                    if lst[k] != lst[j] - 1 or visit[k] == 1:
                        flag = 1
                        break
                # 경사로 가능
                if flag == 0:
                    for k in range(j-L, j):
                        visit[k] = 1
            else:
                # 인덱스가 L보다 작을 때
                flag = 1
                break
        elif lst[j-1] >= lst[j]:
            continue
        else:
            flag = 1
            break
# 행
ans = 0
for i in range(N):
    visit = [0] * N
    flag = 0
    sol(maps[i])
    visit = list(reversed(visit))
    sol(list(reversed(maps[i])))
    if flag == 0:
        ans += 1
for j in range(N):
    visit = [0] * N
    flag = 0
    new_maps = [0] * N
    for i in range(N):
        new_maps[i] = maps[i][j]
    sol(new_maps)
    visit = list(reversed(visit))
    sol(list(reversed(new_maps)))
    if flag == 0:
        ans += 1
print(ans)