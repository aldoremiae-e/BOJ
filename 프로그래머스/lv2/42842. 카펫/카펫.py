def solution(brown, yellow):
    answer = []
    lst = []
    centers = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            if i >= (yellow // i):
                centers.append((i, yellow // i))

    for center in centers:
        # 세로 가로
        a, b = center[0], center[1]
        if (2 * a + 2 * b + 4) == brown:
            answer = [a+2, b+2]

    return answer