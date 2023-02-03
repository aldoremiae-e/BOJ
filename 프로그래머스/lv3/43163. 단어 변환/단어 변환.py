from collections import deque
def bfs(begin, target, words):
    global answer, visit
    q = deque()
    q.append((begin, 0))
    visit.append(begin)
    while q:
        s, c = q.popleft()
        if s == target:
            return c
        for word in words:
            if word in visit:
                continue
            cnt = 0
            for i in range(len(word)):
                if s[i] != word[i]:
                    cnt += 1
            if cnt == 1:
                visit.append(word)
                q.append((word, c+1))
    
def solution(begin, target, words):
    global answer, visit
    visit = []
    answer = 0
    if target not in words:
        answer = 0
    else:
        answer = bfs(begin, target, words)
    return answer