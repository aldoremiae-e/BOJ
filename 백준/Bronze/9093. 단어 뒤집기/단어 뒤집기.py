# sys 모듈 = python 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
# stdin = python 인터프리터가 표준 입력에 사용하는 파일 객체
# readline() = 파일 객체의 메소드 중 하나, read(), readlines()
#               한번에 한 줄 씩 읽는다
import sys
T = int(input())
for tc in range(T):
    sentence = list(map(str,sys.stdin.readline().split()))
    ans = [] # 답
    for word in sentence:
        lst = [] # stack
        for w in word:
            lst.append(w)
        a ='' # 뒤집은 답
        while lst:
            a += lst.pop()
        ans.append(a) # 뒤집은 단어를 넣은 문장
    # 단어를 붙여야한다
    print(f' '.join(ans))