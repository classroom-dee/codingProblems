def run():
    while True:
        n = int(input())
        if n == -1:
            break
        print(is_perfect(n))

def is_perfect(n):
    factors = [i for i in range(1, n) if n % i == 0]
    if sum(factors) == n:
        return f"{n} = {''.join(f'{f} + ' for f in factors).rstrip(' + ')}"
    else:
        return f"{n} is NOT perfect."

run()