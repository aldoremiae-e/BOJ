# 11052
N = int(input())
lst = [0] + list(map(int, input().split()))
memo = [0] * (N+1) # 카드 n팩을 살떄의 최대값
#memo2 = [0] * (N+1)
for i in range(1, N+1):
    for j in range(1, i+1):
        # j번째 팩을 샀을때 + 남은개수를 샀을때의 최대값과 비교해야하기 때문에 memo2는 안됨!
        memo[i] = max(memo[i-j] + lst[j], memo[i])
#        memo2[i] = max(memo2[j] + lst[i-j], memo2[i])

print(memo[N])
