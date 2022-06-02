# 입력값 9개 난쟁이 영어로 dwarf
'''
모든 난쟁이의 키의 합을 구하고
두명 뽑아서 빼보기
'''
# 조합
def comb(arr, n):
    result = []
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i+1:], n - 1):
                result.append([arr[i]] + j)
    return result

dwarf = [0] * 9
sumv = 0
for i in range(len(dwarf)):
    dwarf[i] = int(input())
    sumv += dwarf[i]
re = sumv - 100

# 오름차순으로 정렬
dwarf = sorted(dwarf)
# 2명 조합
# re_dwf 제외되는 2명의 키
two_dwf = comb(dwarf, 2)
for dwf in two_dwf:
    if re == (dwf[0] + dwf[1]):
        re_dwf = dwf
ans = []
for k in range(len(dwarf)):
    if dwarf[k] == re_dwf[0]:
        dwarf[k] = 0
    elif dwarf[k] == re_dwf[1]:
        dwarf[k] = 0
    if dwarf[k] != 0:
        ans.append(dwarf[k])

for l in ans:
    print(l)