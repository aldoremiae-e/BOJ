from sys import stdin
s = stdin.readline().rstrip()
ex = stdin.readline().rstrip()

stack = []
for i in range(len(s)):
    stack.append(s[i])
    if ''.join(stack[-(len(ex)):]) == ex:
        for _ in range(len(ex)):
            stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')