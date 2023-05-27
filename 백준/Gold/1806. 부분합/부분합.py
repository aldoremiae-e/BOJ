N, S = map(int, input().split())
lst = list(map(int, input().split()))

start, end = 0, -1
minLength = int(1e9) #가장 짧은 길이
curSum = 0 # 현재까지의 부분합
while True:
    if curSum < S: # 지금까지의 합이 S보다 작다면
        end += 1 # 다음거를 더하기 위해, 인덱스를 증가
        if end == N: # 다음인덱스가 N을 넘어가면 그만
            break
        curSum += lst[end] # 다음거를 더해줌
    else: # 지금까지의 합이 S보다 크거나 같으면
        minLength = min(minLength, end - start + 1) # 부분합의 길이가 짧은걸 골라줘
        curSum -= lst[start] # start 인덱스 다음거를 봐야하기 위해, 부분합에서 빼주고
        start += 1 # 다음부분합을 보는 거지
print(minLength if minLength != int(1e9) else 0)