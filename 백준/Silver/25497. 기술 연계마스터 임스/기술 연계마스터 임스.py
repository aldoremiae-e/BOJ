N = int(input())
skill = input()
cnt = 0	
Ls, Ss = 0, 0	

for i in skill :
    if i == 'L' :	
        Ls += 1
    elif i == 'R' :
        if Ls > 0 :	
            cnt += 1	
            Ls -= 1	
        else :		
            break	
    elif i == 'S' :	
        Ss += 1
    elif i == 'K' :
        if Ss > 0 :
            cnt += 1	
            Ss -= 1	
        else :		
            break
    else :
        cnt += 1

print(cnt)