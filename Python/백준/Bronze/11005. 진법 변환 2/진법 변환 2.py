n, b = tuple(map(lambda x: int(x), input().split()))

def _namba_reducer(namba: int) -> str:
    if namba < 10:
        return f"{namba}"
    else:
        return chr(namba - 10 + ord("A"))

def _reverse_string(s):
    return ''.join(s[i] for i in range(-1, -len(s)-1, -1))

def convert(n, b):
    nambas = ''
    while n > 0:
        quotient = n // b
        remainder = n % b
        nambas += _namba_reducer(remainder)
        n = quotient
    return _reverse_string(nambas)

print(convert(n, b))