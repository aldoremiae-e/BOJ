N = int(input())
exs = input()
nums = {}
for i in range(N):
    nums[chr(i+65)] = int(input())
stack = []
for s in exs:
    if s == '*':
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)
    elif s == '/':
        b = stack.pop()
        a = stack.pop()
        stack.append(a / b)
    elif s == '+':
        b = stack.pop()
        a = stack.pop()
        stack.append(a + b)
    elif s == '-':
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)
    else:
        stack.append(nums[s])
n = stack.pop()
print(f'{n:.2f}')