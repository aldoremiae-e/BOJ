def solution(fees, records):
    answer = []
    # 0기본시간 1기본요금 2추가시간 3추가요금
    cars = {}
    car_key = []
    for record in records:
        time, number, io = map(str, record.split())
        h, m = map(int, time.split(':'))
        if not number in cars:
            car_key.append(number)
            cars[number] = [[h*60+m, 23*60+59]]
        else:
            if io == 'IN':
                cars[number].append([h*60+m, 23*60+59])
            else:
                cars[number][-1][1] = h*60+m
    car_key.sort()
    for key in car_key:
        res = fees[1]
        t = 0
        for i, o in cars[key]:
            t += o - i

        if t > fees[0]:
            if (t - fees[0]) % fees[2] > 0:
                res += (((t - fees[0]) // fees[2]) + 1) * fees[3]
            else:
                res += ((t - fees[0]) // fees[2]) * fees[3]
            
        answer.append(res)
    return answer