N, S = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
def solve(index, ret):
    global cnt
    if index == N:
        # 정답일 경우
        if ret == S:
            cnt += 1
        # 아닐경우
        return
    solve(index+1, ret+lst[index])
    solve(index+1, ret)
solve(0, 0)
# 예외처리 공집합 - 공집합의 합은 0이라, S가 0이면 하나빼주자.
if S == 0:
    cnt -= 1
print(cnt)