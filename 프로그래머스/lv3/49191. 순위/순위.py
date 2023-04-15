def solution(n, results):
    answer = 0
    maps = [[0] * (n+1) for _ in range(n+1)]
    for result in results:
        i, j = result[0], result[1]
        maps[i][j] = 1
        maps[j][i] = -1
    for k in range(1, n+1): # 중간지점
        for i in range(1, n+1):
            for j in range(1, n+1):
                if maps[i][k] == 1 and maps[k][j] == 1:
                    maps[i][j] = 1
                if maps[i][k] == -1 and maps[k][j] == -1:
                    maps[i][j] = -1
    #노드판에 자기자신, 0 말고 0이 없는 경우
    for i in range(1, n+1):
        flag = 1
        for j in range(1, n+1):
            if i == j:
                continue
            if maps[i][j] == 0:
                flag = 0
                continue
        answer += flag
    return answer