def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    n = len(phone_book)
    for i in range(n-1):
        l = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][:l]:
            answer = False
            break
    return answer