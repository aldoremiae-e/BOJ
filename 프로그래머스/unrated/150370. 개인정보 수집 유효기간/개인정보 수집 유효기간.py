def solution(today, terms, privacies):
    answer = []
    # 현재날짜
    ny, nm, nd = today.split('.')
    ny, nm, nd = int(ny), int(nm), int(nd)
    n = nd + (28 * nm) + (28 * 12) * ny
    # 약관
    dic = {}
    for term in terms:
        op, month = term.split()
        dic[op] = int(month) * 28
    num = 1
    for privacy in privacies:
        cur_days, cur_op = privacy.split()
        cy, cm, cd = cur_days.split('.')
        cy, cm, cd = int(cy), int(cm), int(cd)
        c = cd + (28 * cm) + (28 * 12) * cy
        e = c + dic[cur_op]
        if n >= e:
            answer.append(num)
           # 파기
        
        num += 1
        
    return answer