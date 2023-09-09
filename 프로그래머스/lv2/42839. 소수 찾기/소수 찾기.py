from itertools import permutations as per
def solution(numbers):
    answer = 0
    lst = []
    for number in numbers:
        lst.append(int(number))
    set_num = set()
    for i in range(1, len(numbers)+1):
        for i in set(per(lst, i)):
            s = 0
            for num in i:
                s *= 10
                s += num
            set_num.add(s)
    def isprime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if (n % i) == 0:
                return False
        return True
    
    for i in set_num:
        if isprime(i):
            answer += 1
            
    return answer