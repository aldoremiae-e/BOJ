N = int(input())
arr = [0] * N
for i in range(N):
    a = int(input())
    arr[i] = a
arr.sort()
for i in range(N):
    print(arr[i])