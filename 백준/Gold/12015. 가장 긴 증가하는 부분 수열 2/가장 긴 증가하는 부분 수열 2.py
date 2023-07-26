N = int(input())
lst = list(map(int, input().split()))

memo = [0]
for num in lst:
    if memo[-1] < num:
        memo.append(num)
    else:
        left = 0
        right = len(memo)
        # 이분탐색을 통한 lower_bound
        while left < right:
            mid = (left + right) // 2
            if memo[mid] < num:
                left = mid + 1
            else:
                right = mid
        memo[left] = num
    # 배열에 들어있는 값들은 LIS를 이루는 요소와 무관하다
print(len(memo)-1)