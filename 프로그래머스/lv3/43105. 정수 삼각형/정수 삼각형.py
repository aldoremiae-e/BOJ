def solution(triangle):
    answer = 0
    l = len(triangle)
    tri = [[] for i in range(l)]
    for i in range(1, l):
        for j in range(i+1):
            if j == 0:
                tri[i].append(triangle[i][j] + triangle[i-1][0])
            elif j == i:
                tri[i].append(triangle[i][j] + triangle[i-1][-1])
            else:
                num = max(triangle[i][j] + triangle[i-1][j-1], triangle[i][j] + triangle[i-1][j])
                tri[i].append(num)
        triangle[i] = tri[i]
    answer = max(tri[-1])
                
    return answer