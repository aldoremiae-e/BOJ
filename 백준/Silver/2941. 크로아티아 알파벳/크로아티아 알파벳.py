from sys import stdin
input = stdin.readline().rstrip()
cnt = 0
i = 0

while i < len(input):
    if i == len(input) - 1:
        cnt += 1
        i += 1
    else:
        if input[i] == 'c' and len(input) >= 2:
            if input[i+1] == '=' or input[i+1] == '-':
                cnt += 1
                i += 2
            else:
                cnt += 1
                i += 1
        elif input[i] == 'd' and len(input) >= 2:
            if len(input) >= 3 and input[i+1:i+3] == 'z=':
                cnt += 1
                i += 3
            elif input[i+1] == '-':
                cnt += 1
                i += 2
            else:
                cnt += 1
                i += 1
        elif input[i] == 'l' and len(input) >= 2:
            if input[i+1] == 'j':
                cnt += 1
                i += 2
            else:
                cnt += 1
                i += 1
        elif input[i] == 'n' and len(input) >= 2:
            if input[i+1] == 'j':
                cnt += 1
                i += 2
            else:
                cnt += 1
                i += 1
        elif input[i] == 's' and len(input) >= 2:
            if input[i+1] == '=':
                cnt += 1
                i += 2
            else:
                cnt += 1
                i += 1
        elif input[i] == 'z' and len(input) >= 2:
            if input[i+1] == '=':
                cnt += 1
                i += 2
            else:
                cnt += 1
                i += 1
        else:
            cnt += 1
            i += 1
    if i >= len(input):
        break
print(cnt)