def solution(N, number):
    answer = 0
    DP = [set() for _ in range(9)] # i개의 N을 사용할 때
    #print(DP)
    for i in range(1, 9):
        DP[i].add(int(str(N) * i))
        for j in range(1, i):
            # j번 사용한 배열 @ i-j번 사용한 배열
            # i = 3 일때 (j, i-j) =(1, 2), (2, 1)
            for num1 in DP[j]:
                for num2 in DP[i-j]:
                    DP[i].add(num1 + num2)
                    DP[i].add(num1 - num2)
                    DP[i].add(num1 * num2)
                    if num2 != 0:
                        DP[i].add(num1 // num2)
    #print(DP)
    for i in range(9):
        if number in DP[i]:
            return i
    return -1