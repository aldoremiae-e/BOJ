answer = 0
def dfs(sn, t, numbers, i):
    global answer
    if i == len(numbers) -1:
        if sn == t:
            answer += 1
        return
    dfs(sn+numbers[i+1], t, numbers, i+1)
    dfs(sn-numbers[i+1], t, numbers, i+1)
        
    
def solution(numbers, target):
    global answer
    dfs(numbers[0], target, numbers, 0)
    dfs(-numbers[0], target, numbers, 0)
    return answer