from itertools import permutations as perm
def solution(k, dungeons):
    answer = 0
    visit = [i for i in range(len(dungeons))]
    for idxs in list(perm(visit, len(dungeons))):
        ret = k
        cnt = 0
        for idx in idxs:
            if ret >= dungeons[idx][0]:
                cnt += 1
                ret -= dungeons[idx][1]
            else:
                break
        answer = max(cnt, answer)
    return answer