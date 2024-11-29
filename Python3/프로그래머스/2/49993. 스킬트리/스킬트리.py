# skill tree validity check prob
def solution(order, cases):
    cnt = 0
    for case in cases:
        check = []
        for c in case:
            if c in order:
                check.append(c)
        if len(check) == 0:
            # print("No tree dependent skill. Valid")
            cnt += 1
            continue
        res = ''.join(check)
        # print(res, end=" ")
        if res in order:
            if res[0] == order[0]:
                # print("It is valid.")
                cnt += 1
            # else: print("Not valid. Missing root.")
        # else:
            # print("Not valid. Inorderly.")
    return cnt