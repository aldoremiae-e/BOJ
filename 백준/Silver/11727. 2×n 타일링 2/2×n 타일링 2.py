from sys import stdin

N = int(stdin.readline())
'''
dp[1] = | 1
dp[2] = || = ㅁ 3
dp[3] = ||| =| ㅁ| 
        |ㅁ |=
dp[4] = |||| =|| ㅁ|| |ㅁ| |=| 
        == ||=  ㅁ= 
        ㅁㅁ =ㅁ ||ㅁ
dp[5] = dp[4] + 
        |||= |||ㅁ 
        =|= =|ㅁ 
        ㅁ|= ㅁ|ㅁ 
        |ㅁ= |ㅁㅁ 
        |== |=ㅁ
'''
dp = [0] * (N+3)
dp[1], dp[2]= 1, 3
for i in range(3, N+2):
    dp[i] = dp[i-1] + (2 * dp[i-2])
print(dp[N] % 10007)