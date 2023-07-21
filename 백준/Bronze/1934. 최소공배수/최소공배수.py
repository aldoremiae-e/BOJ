def greatest_common_divisor(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def least_common_multiple(a, b):
    return a * b // greatest_common_divisor(a, b)

T = int(input())
for _ in range(T):
    input_a, input_b = map(int, input().split())
    a = max(input_a, input_b)
    b = min(input_a, input_b)
    ans = least_common_multiple(a, b)
    print(ans)