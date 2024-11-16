def solution(s):
    mx = max(int(n) for n in s.split())
    mn = min(int(n) for n in s.split())
    return f'{mn} {mx}'