def solution(nums):
    answer = 0
    even_mul = 1
    add_mul = 1
    even_num, add_num = 0, 0
    for i in range(len(nums)-1, -1, -1):
        if nums[i] % 2:
            add_num += (nums[i] * add_mul)
            add_mul *= 10
        else:
            even_num += (nums[i] * even_mul)
            even_mul *= 10
    answer = add_num + even_num
    return answer