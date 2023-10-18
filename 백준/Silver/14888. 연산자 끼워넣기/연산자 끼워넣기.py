N = int(input())
A = list(map(int, input().split()))
P, M, MUL, DIV = map(int, input().split()) # + - * //
# 2 1 1 1
# 1_2_3_4_5_6 (5*4*3*2*1) => 총 60가지

def recursion(num, idx, plus, minus, mul, div):
    global maxnum, minnum
    if idx == N:
        maxnum = max(maxnum, num)
        minnum = min(minnum, num)
        return
    # 더하기
    if plus > 0:
        recursion(num + A[idx], idx+1, plus-1, minus, mul, div)
    # 빼기
    if minus > 0:
        recursion(num - A[idx], idx+1, plus, minus-1, mul, div)
    # 곱하기
    if mul > 0:
        recursion(num * A[idx], idx+1, plus, minus, mul-1, div)
    # 나누기
    if div > 0:
        if num >= 0:
            recursion(num // A[idx], idx+1, plus, minus, mul, div-1)
        else:
            recursion(-(abs(num) // A[idx]), idx+1, plus, minus, mul, div-1)

maxnum = -int(1e9) - 1
minnum = int(1e9) + 1
recursion(A[0], 1, P, M, MUL, DIV)
print(maxnum)
print(minnum)