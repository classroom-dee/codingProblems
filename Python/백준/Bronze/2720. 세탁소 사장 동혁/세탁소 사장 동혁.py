def _currency_reducer_pun_intended(change: int) -> str:
    cur = [25, 10, 5, 1]
    n_curs = ''
    n, r = 0, change
    for c in cur:
        n, r = r // c, r % c
        n_curs += f'{n} '
    return n_curs.rstrip()

def run(changes):
    for c in changes:
        print(_currency_reducer_pun_intended(c))

t = int(input())
changes = [int(input()) for _ in range(t)]
run(changes)