def solution(n):
    answer = [[0] * n for _ in range(n)]
    ci, cj = 0, 0
    k = n
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d_idx = 0
    num = 1
    cnt = 0
    while num <= n**2:
        for i in range(k):
            ni, nj = ci + dirs[d_idx][0] * i, cj + dirs[d_idx][1] * i
            answer[ni][nj] = num
            num += 1
        
        if not d_idx % 2:
            k -= 1
        d_idx = (d_idx + 1) % 4
        
        ci, cj = ni + dirs[d_idx][0], nj + dirs[d_idx][1]
        cnt += 1
    return answer