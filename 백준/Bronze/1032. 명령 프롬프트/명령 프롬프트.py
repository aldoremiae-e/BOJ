from sys import stdin

N = int(stdin.readline())
files = [''] * N
for i in range(N):
    files[i] = stdin.readline().rstrip()
correct = list(files[0])
for i in range(1, N):
    for k in range(len(correct)):
        if correct[k] == files[i][k]:
            continue
        else:
            correct[k] = '?'
print("".join(correct))