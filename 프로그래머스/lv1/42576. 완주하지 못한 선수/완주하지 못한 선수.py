def solution(participant, completion):
    answer = 'leo'
    my_dic = {}
    for part in participant:
        if part not in my_dic.keys():
            my_dic[part] = 1
        else:
            my_dic[part] = my_dic[part] + 1
    for comp in completion:
        my_dic[comp] = my_dic[comp] - 1
    for key, val in my_dic.items():
        if val != 0:
            answer = key
    return answer