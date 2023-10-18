N = int(input())
nums = list(map(int, input().split()))
p, mi, m, d = map(int, input().split())
maxnum, minnum = -int(1e9), int(1e9)
# 무시하고 앞에서부터 하는거니까, 누적된 값으로..!

def go(index, cur, plus, minus, mul, div):
    # 답찾을경우
    global maxnum, minnum
    if index == N:
        maxnum = max(maxnum, cur)
        minnum = min(minnum, cur)
        return
    # 불가능할경우가 없음
    # 다음호출
        #조건에 맞게 해줘야한다.
    if plus > 0:
        go(index+1, cur+nums[index], plus-1, minus, mul, div)
    if minus > 0:
        go(index+1, cur-nums[index], plus, minus-1, mul, div)
    if mul > 0:
        go(index+1, cur*nums[index], plus, minus, mul-1, div)
    if div > 0:
        if cur > 0:
            go(index+1, cur//nums[index], plus, minus, mul, div-1)
        else:
            go(index+1, -((-cur)//nums[index]), plus, minus, mul, div-1)

go(1, nums[0], p, mi, m, d)
print(maxnum)
print(minnum)