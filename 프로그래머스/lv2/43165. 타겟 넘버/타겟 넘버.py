def dfs(nums, t, L, s, num):
    global answer
    if s == L:
        if num == t:
            answer += 1
        return
    dfs(nums, t, L, s+1, num + nums[s])
    dfs(nums, t, L, s+1, num - nums[s])
def solution(nums, t):
    global answer
    answer = 0
    L = len(nums)
    dfs(nums, t, L, 0, 0)
    return answer