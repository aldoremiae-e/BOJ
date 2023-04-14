def solution(nums):
    answer = 0
    N = len(nums)
    M = N//2
    # 중복을 제거하는 set 사용.
    set_nums = set(nums)
    sl = len(set_nums)
    # 선택하는 수가 종류수보다 많을 때 최대 종류수 만큼 뽑을 수 있다
    if M > sl:
        answer = sl
    # 선택하는 수보다 종류수가 많을 때 최대 선택하는 수만큼 뽑을 수 있다.
    else:
        answer = M
    return answer