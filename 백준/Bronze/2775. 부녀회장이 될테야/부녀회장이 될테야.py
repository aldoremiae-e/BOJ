from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    k = int(stdin.readline())
    n = int(stdin.readline())
    nums = list(i for i in range(1, n+1))
    for i in range(1, k+1):
        for j in range(1, n):
            nums[j] = nums[j] + nums[j-1]
    print(nums[-1])
