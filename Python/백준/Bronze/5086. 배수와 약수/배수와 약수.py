def is_what(n1, n2):
    if n1 % n2 == 0: return "multiple"
    if n2 % n1 == 0 and n1 != 0: return "factor"
    return "neither"

def run():
    while True:
        n1, n2 = tuple(map(lambda n: int(n), input().split()))
        if n1 == 0 or n2 == 0:
            break
        print(is_what(n1, n2))

run()