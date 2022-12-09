from sys import stdin
from collections import deque
N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
# 임의의 수열이 주어질 때, 수열에서 몇 개의 수를 제거하여 부분 수열을 만들 수 있다.
# arr[i]를 마지막 원소로 가질 때의 가장 긴 증가하는 수열의 크기 , 1로 초기화
dp = [1] * N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            if dp[j]+1 > dp[i]:
                dp[i] = dp[j] + 1
print(max(dp))