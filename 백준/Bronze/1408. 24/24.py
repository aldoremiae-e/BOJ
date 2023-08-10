sh,sm,ss =  map(int, input().split(':'))
eh,em,es = map(int, input().split(':'))
start = ss + sm*60 + sh*3600
end = es + em*60 + eh*3600
ans = end - start
if ans < 0:
    ans = 24*3600 + ans
ansh = ans//3600
ans -= (ansh * 3600)
ansm = ans // 60
anss = ans % 60
print(f'{ansh:02d}:{ansm:02d}:{anss:02d}')