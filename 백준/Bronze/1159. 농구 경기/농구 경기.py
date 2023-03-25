# 성의 첫 글자가 같은 선수 5명
# 성의 첫 글자가 5명보다 적다면 기권
# 뽑을 수 있는 성의 첫 글자

N = int(input())
ans = []
names = {}
for i in range(N):
    name = input().rstrip()
    n = name[0]
    if n not in names.keys():
        names[n] = 1
    else:
        names[n] += 1
for key, val in names.items():
    if val >= 5:
        ans.append(key)
if ans == []:
    print('PREDAJA')
else:
    ans = sorted(ans)
    for i in range(len(ans)):
        print(ans[i], end='')