from sys import stdin
n , m = map(int,stdin.readline().split())
tree = list(map(int,stdin.readline().split()))

def binary(start, end):
    res = 0
    while start <= end:
        mid = (start+end) // 2
        total = 0
        
        for x in tree:
            if x > mid:
                total+= x- mid
            
        if total < m:
            end = mid-1
        else:
            res = mid
            start = mid +1
    return res

print(binary(0, max(tree)))