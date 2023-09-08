def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    sa, sb = 0, 0
    N = len(A)
    ans = 0
    while True:
        if sa == N:
            break
        if A[sa] < B[sb]:
            ans += 1
            sb += 1
        sa += 1
    return ans