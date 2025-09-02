def run():
    n, k = [int(s) for s in input().split()]
    
    def _get_factors(n: int) -> set[int]:
        res = set()
        for i in range(1, n+1):
            if n % i == 0:
                res.add(i)
        return res
    
    factor_list = sorted(_get_factors(n))

    return factor_list[k-1] if len(factor_list) >= k else 0

print(run())
