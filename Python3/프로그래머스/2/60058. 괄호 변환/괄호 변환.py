def solution(p):
    p = ""
    if not p: return p
    return 0# parentheses pairing prob
def solution(p):
    if not p: return p
    dic = {'(': 1, ')': -1}
    cnt = 0
    u, v = '', ''
    for i, c in enumerate(p):
        u += c
        cnt += dic[c]
        if cnt == 0:
            v += p[i+1:]
            break
    # print(u, v)
    if eval_parenth(u):
        return u + solution(v)
    else:
        stuff = '(' + solution(v) + ')'
        for c in u[1:-1]:
            stuff += '(' if c == ')' else ')'
        return stuff

def eval_parenth(s):
    dic = {'(': 1, ')': -1}
    res = 0
    for p in s:
        res += dic[p]
        if res < 0: return False
    return res == 0