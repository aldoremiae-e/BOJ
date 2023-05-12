def solution(my_string, is_prefix):
    ms = []
    ip = []
    for i in range(len(my_string)):
        ms.append(my_string[i])
    for j in range(len(is_prefix)):
        ip.append(is_prefix[j])
    n, m = len(ms), len(ip)
    if n < m:
        return 0
    else:
        flag = True
        for i in range(m):
            if ip[i] != ms[i]:
                flag = False
                break
        if flag:
            return 1
        else:
            return 0