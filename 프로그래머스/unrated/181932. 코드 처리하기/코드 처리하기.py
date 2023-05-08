def solution(code):
    answer = ''
    mode = False
    for idx in range(len(code)):
        if mode == False:
            if code[idx] == '1':
                mode = True
            else:
                if not idx % 2:
                    answer += code[idx]
        else:
            if code[idx] == '1':
                mode = False
            else:
                if idx % 2:
                    answer += code[idx]
    if answer == '':
        answer = 'EMPTY'
    return answer