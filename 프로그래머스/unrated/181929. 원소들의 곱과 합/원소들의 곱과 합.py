def solution(num_list):
    answer = 0
    mul_num = 1
    mul_sq = 0
    for i in range(len(num_list)):
        mul_num *= num_list[i]
        mul_sq += num_list[i]
    mul_sq = mul_sq * mul_sq
    if mul_num < mul_sq:
        answer = 1
    return answer