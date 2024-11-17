# jaded case prob
def solution(s):
    s = list(s)
    for i, c in enumerate(s):
        if i != 0: 
            if s[i] != s[i-1] and s[i-1] == ' ':
                s[i] = c.upper()
            else:
                s[i] = c.lower()
        else:
            s[i] = c.upper()
    return ''.join(s)