import sys
bracket = list(sys.stdin.readline())
cnt = 0
ans = 0
for i in range(len(bracket)):
    if bracket[i] == '(':
        cnt += 1

    elif bracket[i] == ')':
        if bracket[i-1] == '(':
            # i-1과 i는 레이저
            cnt -= 1
            ans += cnt

        else:
            # 닫힌괄호
            ans += 1
            cnt -= 1

print(ans)