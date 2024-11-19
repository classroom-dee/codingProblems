# the carpet conundrum
def solution(brown, yellow):
    for i in range(1, yellow+1):
        if yellow % i == 0:
            div = yellow // i
            if config(div, i) == brown - 4:
                return [div + 2, i + 2] if div > i else [i + 2, div + 2]
def config(x, y):
    return x * 2 + y * 2