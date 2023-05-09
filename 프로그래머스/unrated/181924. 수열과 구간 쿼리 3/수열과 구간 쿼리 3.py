def solution(arr, queries):
    for q in queries:
        i, j = q[0], q[1]
        new = []
        for a in range(len(arr)):
            if a == i:
                new.append(arr[j])
            elif a == j:
                new.append(arr[i])
            else:
                new.append(arr[a])
        arr = new
    return arr