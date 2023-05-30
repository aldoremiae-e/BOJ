N = int(input())

# dp문제임은 알았다
# 갱신해갈것
dp_max = [0] * 3
sum_max = [0] * 3
dp_min = [0] * 3
sum_min = [0] * 3
for i in range(N):
    a, b, c = map(int, input().split())
    for j in range(3):
        if j == 0:
            sum_max[j] = a + max(dp_max[j], dp_max[j+1])
            sum_min[j] = a + min(dp_min[j], dp_min[j+1])

        elif j == 1:
            sum_max[j] = b + max(dp_max[j-1], dp_max[j], dp_max[j+1])
            sum_min[j] = b + min(dp_min[j-1], dp_min[j], dp_min[j+1])

        else:
            sum_max[j] = c + max(dp_max[j], dp_max[j-1])
            sum_min[j] = c + min(dp_min[j], dp_min[j-1])

    for j in range(3):
        dp_max[j] = sum_max[j]
        dp_min[j] = sum_min[j]
print(max(dp_max), min(dp_min))