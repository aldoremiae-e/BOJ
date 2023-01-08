# LCS
from sys import stdin

A = stdin.readline().rstrip()
B = stdin.readline().rstrip()

arr = list([0] * (len(A) + 1) for _ in range(len(B) + 1))
for j in range(len(B)):
    for i in range(len(A)):
        if B[j] != A[i]:
            arr[j+1][i+1] = arr[j+1][i] if arr[j+1][i] > arr[j][i+1] else arr[j][i+1]
        else:
            arr[j+1][i+1] = arr[j][i] + 1
print(arr[-1][-1])