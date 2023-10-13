def solution(genres, plays):
    answer = []
    dict = {}
    g_dict = {}
    N = len(genres)
    for i in range(N):
        if genres[i] not in dict:
            dict[genres[i]] = []
            g_dict[genres[i]] = 0
        dict[genres[i]].append((plays[i],i))
        g_dict[genres[i]] += plays[i]
    for key, val in dict.items():
        val.sort(key=lambda x:(-x[0], x[1]))
    lst = [(val, key) for key, val in g_dict.items()]
    lst.sort(reverse=True)
    for _, genre in lst:
        for i in range(2):                
            answer.append(dict[genre][i][1])
            if len(dict[genre]) == 1:
                break
    return answer