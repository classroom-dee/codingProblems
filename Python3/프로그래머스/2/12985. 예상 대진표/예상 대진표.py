def solution(n, a, b):
    round = 1
    f = lambda x: x // 2 if x % 2 == 0 else (x + 1) // 2
    while True:
        if abs(a - b) == 1 and (f(a) == f(b)):
            return round
        round += 1
        a, b = f(a), f(b)