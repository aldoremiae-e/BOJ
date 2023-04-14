def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command[0]-1, command[1], command[2]-1
        new = []
        for t in range(i, j):
            new.append(array[t])
        new = sorted(new)
        answer.append(new[k])
    return answer