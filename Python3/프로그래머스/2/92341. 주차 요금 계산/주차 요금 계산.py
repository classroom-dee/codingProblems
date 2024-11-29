def solution(fees, records):
    import math
    dic = {}
    for r in records:
        targ = r.split()
        if not dic.get(targ[1]): dic[targ[1]] = [targ[0].split(':')]
        else:
            dic[targ[1]].append(targ[0].split(':'))
    dic = sorted(dic.items(), key=lambda x: int(x[0]))
    res = []
    for car in dic:
        if len(car[1]) % 2 != 0:
            car[1].append(['23', '59'])
        t = 0
        for i in range(1, len(car[1]), 2):
            min = (int(car[1][i][0]) * 60 + int(car[1][i][1])) - (int(car[1][i-1][0]) * 60 + int(car[1][i-1][1]))
            t += min
        if t <= fees[0]:
            res.append(fees[1])
        else:
            excess = t - fees[0]
            if excess % fees[2] != 0:
                res.append(fees[1] + math.ceil((t - fees[0]) / fees[2]) * fees[3])
            else:
                res.append(fees[1] + ((t - fees[0]) // fees[2]) * fees[3])
    return res