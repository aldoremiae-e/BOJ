def solution(m, n, puddles):
    answer = 0
    maps = [[0] * (m+1) for _ in range(n+1)]
    
    for j in range(1, m+1):
        for i in range(1, n+1):
            if i == 1 and j == 1:
                maps[1][1] = 1
                continue
            #print(i, j)
            if [j, i] in puddles:
                continue
            else:
                maps[i][j] = (maps[i-1][j] + maps[i][j-1]) % 1000000007
    
    answer = maps[n][m]
    return answer