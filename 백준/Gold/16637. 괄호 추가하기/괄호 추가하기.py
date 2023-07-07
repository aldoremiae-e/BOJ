# + - 만 잇을 떄 -가 나오기 전까지 괄호를 닫았다.
# + - * 가 있을 때 * 가 있으면 괄호를 열고 -가 나오기 전까지 괄호를 닫는다
#  단, 괄호 안에는 연산자가 하나만 들어 있어야 한다.
from collections import deque

def solve_first(num_lst, op_lst):
    num = num_lst[0]
    for i in range(len(op_lst)):
        op = op_lst[i]
        num = solve(num, num_lst[i+1], op)
    return num

def solve(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2

# 괄호위치 찾기
def dfs(n, idx):
    global ans
    if n == len(ops):
        return
    for i in range(idx, len(ops)):
        visit.append(i)
        dfs(n+1, i+2)
        # 계산하자
        l = (len(nums) - len(visit))
        num_lst = [0] * l
        k = 0
        for i in range(l):
            if k in visit:
                num_lst[i] = bracket_nums[k]
                k += 2
            else:
                num_lst[i] = nums[k]
                k += 1
        op_lst = []
        for i in range(len(ops)):
            if i in visit:
                continue
            op_lst.append(ops[i])
        ans = max(ans, solve_first(num_lst, op_lst))
        visit.pop()

N = int(input())
exp = input()
nums = deque()
ops = deque()
for i in range(N):
    if i % 2:
        ops.append(exp[i])
    else:
        nums.append(int(exp[i]))
visit = []
ans = solve_first(nums, ops)

bracket_nums = []
for i in range(len(ops)):
    op = ops[i]
    bracket_nums.append(solve(nums[i], nums[i+1], op))

dfs(0, 0)
print(ans)