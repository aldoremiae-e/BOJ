word=input()
words=[]

for i in range(1,len(word)):
    A=word[:i][::-1]
    for j in range(i, len(word)-1):
        B=word[i:j+1][::-1]
        C=word[j+1:][::-1]
        words.append(A+B+C)
        
words.sort()
print(words[0])