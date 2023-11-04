def solution(sequence, k):
    answer = [0, 0]
    cnt = sequence[0]
    start, end = 0, 0
    leng = int(1e9)
    while start <= end < len(sequence):
        if cnt == k:
            # 인덱스 길이 짧은거
            e = end - start + 1
            if e < leng:
                leng = e
                answer[0] = start
                answer[1] =  end
            cnt -= sequence[start]
            start += 1
        elif cnt < k:
            end += 1
            if end == len(sequence):
                break
            cnt += sequence[end]
        else:
            cnt -= sequence[start]
            start += 1
    return answer