def solution(A,B):
    answer = 0
    A = sorted(A, reverse=True)
    B = sorted(B)
    for i in range(len(A)):
        answer += (A[i] * B[i])            
    return answer