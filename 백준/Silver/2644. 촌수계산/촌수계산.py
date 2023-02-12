from sys import stdin

n = int(stdin.readline())
a, b = map(int, stdin.readline().split())
m = int(stdin.readline())
family =[[] for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, stdin.readline().split())
    family[i].append(j)
    family[j].append(i)
visit = [0] * (n+1)

def dfs(s, e, cnt):
    global ans
    if family[s]:
        if e in family[s]:
            cnt += 1
            ans = cnt
            return ans
        else:
            for fs in family[s]:
                if visit[fs] == 0:
                    visit[fs] = 1
                    dfs(fs, e, cnt+1)
                    visit[fs] = 0
ans = -1
visit[a] = 1
dfs(a, b, 0)
print(ans)