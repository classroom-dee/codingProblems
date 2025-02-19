def solution(N, number):
    if N == number: return 1
    # init a list of sets
    s = [set() for _ in range(8)]
    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))
        
    # op and add
    for i in range(1, len(s)):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        if number in s[i]: # early break on asnwer found
            res = i + 1
            break
    else: # for when there's no answer in any of the sets 
        res = -1
    return res