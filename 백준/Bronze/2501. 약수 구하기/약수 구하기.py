ans = []
re = 0
# 입력 값
N, K = map(int, input().split())

# 약수 구하기
for i in range(1, N+1):
    if N % i == 0:
        ans.append(i)

# 약수 중 K번째로 작은 수
for idx in range(len(ans)):
    if idx == (K-1):
        re = ans[idx]
print(re)