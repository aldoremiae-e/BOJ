def solution(nums):
    answer = nums
    if nums[-1] > nums[-2]:
        answer.append(nums[-1] - nums[-2])
    else:
        answer.append(nums[-1] * 2)
    return answer