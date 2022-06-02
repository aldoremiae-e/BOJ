'''
최대 공약수 공통된 약수 중 가장 큰 수
최소 공배수 두 수 의 곱 / 최대 공약수
'''

N, M = map(int, input().split())
arr1, arr2 = [], []
for i in range(1, N+1):
    if N % i == 0:
        arr1.append(i)
for j in range(1, M+1):
    if M % j == 0:
        arr2.append(j)
gcm = 0
for i in arr1:
    for j in arr2:
        if i == j:
            gcm = i if i > gcm else gcm

lcm = (N * M) // gcm
print(gcm)
print(lcm)