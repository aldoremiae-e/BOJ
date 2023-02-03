def dfs(cur, computers):
    global visit
    visit[cur] = 1
    for k in range(len(computers)):
        if computers[cur][k] == 1 and visit[k] == 0:
            dfs(k, computers)
def solution(n, computers):
    global visit
    answer = 0
    visit = [0] * n
    for i in range(n):
        if visit[i] == 0:
            dfs(i, computers)
            answer += 1
    return answer