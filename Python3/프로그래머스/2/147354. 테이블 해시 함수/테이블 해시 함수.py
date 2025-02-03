def solution(data, col, row_begin, row_end):
    l = len(data)
    for i in range(l):
        for j in range(i, l):
            if data[i][col - 1] > data[j][col - 1]:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
            elif data[i][col - 1] == data[j][col - 1]:
                if data[i][0] <= data[j][0]:
                    temp = data[i]
                    data[i] = data[j]
                    data[j] = temp
    S_i = [sum([e % (i + 1) for e in row]) for (i, row) in enumerate(data)]
    res = S_i[row_begin - 1]
    for i in range(row_begin, row_end):
        res ^= S_i[i]
    return res