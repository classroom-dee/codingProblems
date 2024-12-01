def solution(record):
    d = {}
    for m in record:
        info = m.split()
        if info[0] == 'Enter' or info[0] == 'Change':
            d[info[1]] = info[2]
    def massage(x):
        info = x.split()
        if info[0][0] == 'C': return
        else:
            user = d[info[1]]
            msg = '님이 들어왔습니다.' if info[0][0] == 'E' else '님이 나갔습니다.'
            return user + msg
    return list(filter(lambda x: x is not None, map(massage, record)))